# Responsibility Pools
— 「責任の引受先」を“点”ではなく“場所”として設計する —

VCDesign は、責任を「明確な個人」に固定することを最初から要求しない。

責任は、組織の成熟度や運用状態によって、
最初はぼんやりしていてもよい。

ただし、VCDesign が要求する最低条件がある。

> **責任が引き受けられる“場所”が存在し、  
>  そこへ返す手続きが明示されていること。**

この「場所」を、ここでは **責任プール（Responsibility Pool）** と呼ぶ。

---

## なぜプールが必要か

責任が曖昧な組織（Phase 0/1/2）では、
「責任者を決めろ」と言った瞬間に政治になる。

しかし現実の運用では、
責任はすでに発生している。

- 誰かが暗黙に引き受けている
- あるいは、誰も引き受けずに蒸発している

VCDesign は、この蒸発を許容しない。

そのために、
責任を「一点の個人」へ固定する前に、
まず **引き受け先の“場所”** を設計する。

---

## プールとは何か（定義）

責任プールとは：

- 個人ではない（最初から特定しない）
- しかし「どこにも属さない」でもない
- 引き受ける可能性を持つ主体集合（役割・当番・チーム）である

プールは、曖昧さの逃げではない。

曖昧さを **追跡可能な状態**へ変換するための構造である。

---

## RP との関係（重要）

Resolution Protocol（RP）は、
判断不能を「失敗」ではなく「正規の遷移」として扱う。

責任プールは、その遷移先として使われる。

- `return_to_human`：特定の人へ返す
- `return_to_pool`：責任プールへ返す（受領・割当待ち）

ただし VCDesign において：

> **プールへ投げ込まれた状態は Resolution（解決）ではない。**

プールに返すことは、
「解決済み」ではなく、
**解決待ちを正式に記録した状態**である。

---

## 「ぼんやり責任」を許容する条件

責任がぼんやりしていてもよいのは、
次の条件を満たす場合に限る。

1. **返却先（pool）が定義されている**
2. **受領（ack）されるまで責任が確定しない**
3. **受領されない滞留を可視化できる**
4. **滞留が老化（aging）し、次の処置へ遷移できる**

これにより、
責任の曖昧さは “不明” ではなく “状態” になる。

---

## 最小定義（manifest / binding 側に置く）

プールの定義は、
プロジェクトや組織に依存するため、
Core の不変仕様ではなく **manifest / binding 側**に置く。

ここでは、RP が参照するための **最小形**のみ示す。

```yaml
responsibility_pools:
  - pool_id: "ops_oncall"          # RP.target_pool_id で参照される不変ID
    name: "Ops On-Call Pool"
    description: "Service continuity incidents requiring human ownership."
    default_urgency: "high"        # low|high（RPが省略した場合の既定）

    acceptance:
      requires_ack: true           # 受領（ack）されるまで責任は確定しない
      ack_sla_minutes: 30          # 受領SLA（超過は滞留＝状態として扱う）

    assignment:
      mode: "rotation"             # rotation|manual|role_based
      on_empty_assignment: "queue_and_wait"

    aging:
      ttl_minutes: 240             # 放置の老化（責任の蒸発を防ぐ最小装置）
      on_ttl_expired: "escalate"   # escalate|notify_only
      escalate_to_pool_id: "ops_manager"

    audit:
      record_required: true
