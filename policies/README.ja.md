# policies/

Policies は、**交渉不可能な判断境界**を定義します。

これらは、以下の場合に評価されます：
- 自動化された最適化が提案された場合
- AI生成されたアクションがレビューされる場合
- 価値間のトレードオフが要求された場合

Policies はガイドラインではありません。
Policies はベストプラクティスではありません。
Policies は、**拒否、停止、または明示的な責任の要求**のために存在します。

---

## boundary-lexicographic-policy

このポリシーは、境界の辞書順序を強制します：

SAFETY（安全性） > COMPLIANCE（法令遵守） > TRUST（信頼） > ETHICS（倫理） > BUSINESS_VIABILITY（事業成立性） > KPI_EFFICIENCY（KPI効率）

下位の改善は、決して上位の境界を侵害してはなりません。

- `.md` : 人間可読な正当化根拠
- `.json` : 正本となる機械可読ポリシー
- `.rego` : 実行可能な強制ロジック
