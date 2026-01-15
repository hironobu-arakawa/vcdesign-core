# VCDesign (VCD) Core
**Value Continuity Design (価値継続設計)**

> **「作る」ことが一瞬で終わる世界で、価値を「渡し続ける」ための設計コア**

VCDesign (VCD) は、運用が継続し、コンテキストが変化し、判断を完全に自動化できないシステムにおいて、長期にわたって価値を持続させるための設計思想（および実装エコシステム）です。

VCDesign はデリバリーの最適化を目指すものではありません。
デリバリー後の **価値の摩耗 (value erosion)** を防ぐために存在します。

**公式サイト:** [日本語](https://vcdesign.org/ja)

---

## なぜ今、VCDesignが必要なのか

### 常時高速最適化 (Always-on Rapid Optimization)
生成AIと自動化技術により、システムは「改善が無期限に、無償で、即時に行われる」世界に突入しました。
この環境下では、最適化が止まることはなく、誰も「止める責任」を持たない状態が生まれやすくなります。

### 判断の境界 (Decision Boundaries)
「誰がその決定を下したのか」「責任はどこにあるのか」が曖昧なまま自動化が進むと、システムは動いていても価値は断絶します。
VCDesign は、**決定が最終的なものになることが許される場所（境界）** を明示的に設計します。

詳細な背景哲学については、以下を参照してください。
➡️ [PHILOSOPHY.ja.md](./docs/philosophy/PHILOSOPHY.ja.md)

---

## コア・アーキテクチャ (The Ecosystem)

VCDesign Core は単なる思想ではなく、以下の3つの層で構成されるエコシステムです。

### 1. 🛡️ Constitution (憲法と優先順位)

トレードオフが発生した際、都度計算するのではなく構造によって判断するための「辞書式優先順位 (Lexicographic Order)」を定義します。
上位の境界は、下位の最適化のために決して侵害されてはなりません。

1. 🔴 **SAFETY (安全・人命)** [Hard Constraint]
2. 🔴 **COMPLIANCE (法令・規制)** [Hard Constraint]
3. 🔴 **TRUST (信用・監査性)** [Hard Constraint]
4. 🔴 **ETHICS (倫理・公正)** [Hard Constraint]
5. 🟡 **BUSINESS_VIABILITY (事業成立性)** [Soft Constraint]
6. 🟢 **KPI / EFFICIENCY (効率)** [Soft Constraint]

> **Note:** KPIは常に最下位に置かれ、すべての上位フィルタを通過する必要があります。

*参照: [policies/boundary-lexicographic-policy.md](./policies/boundary-lexicographic-policy.md)*

### 2. 🔌 Domain Bindings (ドメインバインディング)

汎用的なCoreを特定の業務領域に適応させるための定義ファイル群です。「何がFact（不変の事実）で、何がHypothesis（解釈）か」をドメインごとに規定します。

| Binding ID | Domain | 特徴 / Factの定義 |
| :--- | :--- | :--- |
| **analytics_llm** | 分析・汎用 | 基本形。AI出力は常に「仮説」であり、人間が「解決(Resolution)」する。 |
| **finance** | 金融 | 台帳(Ledger)が権威。資金移動には厳格な監査証跡と責任者を要求。 |
| **healthcare** | 医療 | 臨床記録がFact。AIによる診断は禁止され、医師の署名が必須。 |
| **legal** | 法務 | 文書・条文がFact。法的助言には引用(Citation)と弁護士の確認が必要。 |
| **factory** | 製造(OT/IT) | 物理センサー値がFact。ITからの制御信号は安全境界を越える必要がある。 |
| **public_sector** | 公共 | 公的記録がFact。正当な手続きと透明性が最適化より優先される。 |
| **enterprise_decision** | 経営 | 実績データがFact。戦略決定は「責任ある主体のコミットメント」として扱う。 |

*参照: [bindings/](./bindings/)*

### 3. ⚖️ Policy Evaluator (参照実装)

提案された変更（Proposal）が、定義された憲法（Policy）に違反していないかを機械的に判定するツールです。CI/CDパイプラインやAIエージェントのガードレールとして機能します。

* **Input:** Proposal (JSON), Policy (YAML/JSON)
* **Output:** `ALLOW` / `REVIEW` / `DENY` および違反理由
* *参照: [tools/policy-evaluator/](./tools/policy-evaluator/)*

---

## 概念的基盤 (The Manifesto)

VCDesign は、エンジニアリングにおける「単位」と「役割」を再定義します。

* **Chapter (章)**
  フェーズやバージョンではなく、「判断と責任のセット」を管理単位とします。価値はChapterをまたいで手渡されます。
* **Operation (運用)**
  単なる保守作業ではなく、過去の判断を現在の現実に照らして「引き受け直す（または返す）」創造的行為です。
* **The Continuer (継続する者)**
  Builder（作る人）でもOperator（回す人）でもなく、価値が断絶しないよう判断と責任を繋ぎ続ける新しいエンジニア像です。

---

## このリポジトリの使用方法

このリポジトリには、VCDesign の不変のコアが含まれています。

### 1. AIへのコンテキスト注入 (Context Injection)
設計レビューやコード生成を行う生成AIに対して、`constitution/` や `bindings/` を読み込ませ、「The Continuer」として振る舞うよう指示します。

### 2. アーキテクチャレビューの基準として
人間がシステム設計を行う際のチェックリスト、およびチーム間での合意形成（Design Contract）の土台として使用します。

### 3. 自動ガードレールとして (Policy Evaluator)
AIエージェントや自動化スクリプトが生成した提案を `evaluator.py` に通し、憲法に違反していないかを自動的に検証します。

---

## ディレクトリ構造

├── bindings/       # 各ドメイン向けの適用ルール (YAML/README)
├── constitution/   # 核となる価値判断基準・優先順位 (YAML/Markdown)
├── docs/           # 哲学、マニフェスト、診断ガイド
├── examples/       # 具体的なProposalのJSON例
├── policies/       # Policy Evaluator用のポリシー定義
├── prompts/        # LLMに与えるプロンプト例
└── tools/          # Policy Evaluator (参照実装)

Status
Version: 2.0 (Canonical)

Phase Diagnosis: あなたの組織がどのフェーズにいるかを知るには、フェーズ診断 (Diagnosis) を参照してください。