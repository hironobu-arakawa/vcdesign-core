import enum
import hashlib
import secrets
import json
from dataclasses import dataclass, asdict
from typing import Optional, Tuple
from abc import ABC, abstractmethod

# ==========================================
# 1. BOA Context Definition (The "Why" & "Where")
# ==========================================

@dataclass(frozen=True)
class BOABoundary:
    """
    BOAにおける「境界」の定義。
    これが一致しない限り、物理的に接続できても論理的に接続してはならない。
    """
    responsibility_boundary_id: str  # 責任境界ID (例: "sys.secure.code.v1")
    meaning_scope_id: str            # 意味の定義 (例: "executable_python_3.x")
    context_assumption_id: str       # 前提条件 (例: "input_is_utf8_string")

    def to_string(self) -> str:
        # 署名用に一意な文字列化
        return f"{self.responsibility_boundary_id}::{self.meaning_scope_id}::{self.context_assumption_id}"

# ==========================================
# 2. Cryptography & Claim
# ==========================================

class Ed25519Mock:
    @staticmethod
    def keygen():
        priv = secrets.token_hex(16)
        pub = hashlib.sha256(priv.encode()).hexdigest()[:16]
        return priv, pub

class PublicVerifier:
    def __init__(self, pub_key): self._pub = pub_key

    def verify(self, claim: 'Claim') -> bool:
        """
        検証対象: Digest + AuditLog + Boundary (これら全てが改ざんされていないか)
        """
        if not claim.signature or not claim.content_digest: return False
        
        # 署名対象のペイロードを再構築
        payload = f"{claim.content_digest}::{claim.audit_log}::{claim.boundary.to_string()}"
        
        expected_part = hashlib.sha256(f"{payload}::{self._pub}".encode()).hexdigest()[:10]
        return claim.signature.endswith(expected_part)

class PrivateNotary:
    def __init__(self, priv, pub):
        self._priv = priv
        self._pub = pub

    def sign(self, digest: str, audit_log: str, boundary: BOABoundary) -> str:
        """Boundaryを含めて署名する"""
        payload = f"{digest}::{audit_log}::{boundary.to_string()}"
        
        sig_hash = hashlib.sha256(f"{payload}::{self._priv}".encode()).hexdigest()
        verify_part = hashlib.sha256(f"{payload}::{self._pub}".encode()).hexdigest()[:10]
        return f"{sig_hash}-{verify_part}"

class ClaimSignal(enum.Enum):
    SIGNED = "✅ SIGNED"
    DENIED = "🚫 DENIED"
    SILENCE = "💀 SILENCE"

@dataclass(frozen=True)
class Claim:
    signal: ClaimSignal
    audit_log: str
    boundary: BOABoundary          # 【New】BOA境界定義
    content_digest: Optional[str]
    signature: Optional[str]

# ==========================================
# 3. Interfaces (DI)
# ==========================================

class ILLMProvider(ABC):
    @abstractmethod
    def call(self, prompt: str) -> str: pass

class ICoreStrategy(ABC):
    @abstractmethod
    def generate(self, task: str, llm: ILLMProvider) -> str: pass

class ISensorStrategy(ABC):
    def set_notary(self, notary: PrivateNotary): self._notary = notary
    
    @abstractmethod
    def audit(self, content: str, boundary: BOABoundary, llm: ILLMProvider) -> Claim:
        pass

# ==========================================
# 4. Implementations (BOA Compliant)
# ==========================================

class BOACompliantSensor(ISensorStrategy):
    def __init__(self): self._notary = None

    def audit(self, content: str, boundary: BOABoundary, llm: ILLMProvider) -> Claim:
        # 1. Silence Check
        if content is None:
            return Claim(ClaimSignal.SILENCE, "Null Output", boundary, None, None)

        # 2. Meaning Scope Check (BOA Logic)
        # 境界IDが "code.v1" なら、コードであることを厳密にチェック
        if "code" in boundary.meaning_scope_id:
            if "def" not in content:
                # 意味の境界を越えた (Drift)
                return Claim(ClaimSignal.DENIED, "Meaning Drift: Not Code", boundary, None, None)
        
        # 3. Signed
        audit_log = "PASS: Content matches Meaning Scope"
        digest = hashlib.sha256(content.encode()).hexdigest()
        
        # 境界情報(boundary)も含めて署名する
        signature = self._notary.sign(digest, audit_log, boundary)
        
        return Claim(ClaimSignal.SIGNED, audit_log, boundary, digest, signature)

class MockLLM(ILLMProvider):
    def call(self, p): return "..."

class PythonCore(ICoreStrategy):
    def generate(self, task, llm):
        if "drift" in task: return "Just a text message."
        return "def process_data(): pass"

# ==========================================
# 5. CCP Artifact (Server-Side Integrity)
# ==========================================

class BOAArtifact:
    def __init__(self, name, boundary: BOABoundary, llm, core, sensor):
        self.name = name
        self.boundary = boundary # このArtifactが背負う「責任境界」
        self._core = core
        self._sensor = sensor
        self._llm = llm
        
        priv, pub = Ed25519Mock.keygen()
        self._notary = PrivateNotary(priv, pub)
        self._public_verifier = PublicVerifier(pub)
        self._sensor.set_notary(self._notary)
        
        self._last_result = (None, None)

    def execute(self, task):
        print(f"\n--- {self.name} Executing Task ---")
        content = self._core.generate(task, self._llm)
        # Sensorに境界定義(self.boundary)を渡して監査させる
        claim = self._sensor.audit(content, self.boundary, self._llm)
        self._last_result = (claim, content)
        print(f"   Claim: {claim.signal.value} | Boundary: {claim.boundary.responsibility_boundary_id}")

    def get_interface(self) -> Tuple[Claim, PublicVerifier]:
        claim, _ = self._last_result
        if claim is None:
             claim = Claim(ClaimSignal.SILENCE, "No Run", self.boundary, None, None)
        return claim, self._public_verifier

    def pull_data(self) -> str:
        """
        【Pipe Self-Audit】
        サーバー側で提供直前に再ハッシュ計算を行い、Claimと矛盾がないか強制確認する。
        """
        claim, content = self._last_result
        
        # 1. 状態チェック
        if not claim or claim.signal != ClaimSignal.SIGNED:
            raise ConnectionError("Pipe Closed: Not SIGNED")

        # 2. 【重要】サーバーサイド完全性チェック (Digest Mismatch Prevention)
        current_digest_check = hashlib.sha256(content.encode()).hexdigest()
        
        if current_digest_check != claim.content_digest:
            # メモリ破壊、改ざん、あるいはCoreが監査後にこっそり書き換えた場合など
            print(f"   [CRITICAL] Server Integrity Check FAILED. Pipe assumes breach.")
            raise RuntimeError("INTERNAL INTEGRITY ERROR: Content digest mismatch.")

        # 3. 出荷
        return content

# ==========================================
# 6. Client (BOA Awareness)
# ==========================================

def boa_connection_protocol(artifact, task_name, expected_boundary_id):
    # 1. Execute
    artifact.execute(task_name)
    
    # 2. Get Interface
    claim, verifier = artifact.get_interface()

    # 3. 【BOA Check】境界IDの一致確認
    # 相手がどんなに素晴らしいコードを書いても、求めている「責任境界」と違えば接続しない
    if claim.boundary.responsibility_boundary_id != expected_boundary_id:
        print(f"[Client] 🚫 BOUNDARY MISMATCH. Expected '{expected_boundary_id}', got '{claim.boundary.responsibility_boundary_id}'")
        return

    # 4. Signal Check
    if claim.signal != ClaimSignal.SIGNED:
        print(f"[Client] 🚫 Signal is {claim.signal.value}")
        return

    # 5. Verify Signature (Digest + Boundary + Log)
    if not verifier.verify(claim):
        print("[Client] ⚠️ SECURITY ALERT: Signature Invalid.")
        return

    # 6. Pull Data (Pipe Open)
    print(f"[Client] ✅ Boundary & Signature Verified. Requesting Data...")
    try:
        data = artifact.pull_data() # Server-side check runs here
        print(f"[Client] 📦 RECEIVED: {data}")
    except RuntimeError as e:
        print(f"[Client] 💥 SERVER ERROR: {e}")
    except ConnectionError as e:
        print(f"[Client] 💥 CONNECTION ERROR: {e}")

# ==========================================
# 7. Execution Scenarios
# ==========================================

if __name__ == "__main__":
    # 定義: 安全なPythonコードの境界
    SAFE_PYTHON_ZONE = BOABoundary(
        responsibility_boundary_id="sys.secure.code.v1",
        meaning_scope_id="executable_python_3.x",
        context_assumption_id="utf8_input_only"
    )

    # 定義: 別の境界 (例: 自然言語チャット)
    CHAT_ZONE = BOABoundary(
        responsibility_boundary_id="sys.general.chat.v1",
        meaning_scope_id="natural_language",
        context_assumption_id="any_input"
    )

    # Artifactの生成 (Python Zoneに住むエージェント)
    agent = BOAArtifact("Dev-Bot", SAFE_PYTHON_ZONE, MockLLM(), PythonCore(), BOACompliantSensor())

    # Scenario 1: Success (Boundary Match & Content Valid)
    print("\n=== Scenario 1: Perfect Match ===")
    boa_connection_protocol(agent, "gen_code", expected_boundary_id="sys.secure.code.v1")

    # Scenario 2: Boundary Mismatch (Client wants Chat, Agent offers Code)
    print("\n=== Scenario 2: Boundary Mismatch ===")
    boa_connection_protocol(agent, "gen_code", expected_boundary_id="sys.general.chat.v1")

    # Scenario 3: Internal Integrity Check (Server side protection)
    # 強制的に改ざんをシミュレート
    print("\n=== Scenario 3: Internal Corruption Attack ===")
    agent.execute("gen_code")
    # 監査後にこっそり中身を書き換える攻撃
    agent._last_result = (agent._last_result[0], "import virus # MALICIOUS INJECTION")
    
    try:
        agent.pull_data()
    except RuntimeError as e:
        print(f"Server Self-Defense Triggered: {e}")