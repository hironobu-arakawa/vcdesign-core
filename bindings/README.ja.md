# bindings/

Bindings は、VCDesign Core を特定のコンテキストにどのように適用するかを定義します。

- これらは実装ではありません。
- これらは仕様ではありません。
- これらは例示ではありません。

Bindings は以下を記述します：
- どの制約が不変であるか
- どの前提が変化するか
- 責任と検証がどこに置かれるか

---

## Binding のカテゴリ

### Capability / Technology bindings
- analytics_llm/
  - Fact / Meaning / Responsibility の分離を維持しながら LLM を使用する方法

### Organizational / Governance bindings
- enterprise_decision/
  - VCDesign を企業レベルの意思決定プロセスに適用する方法

### Industry bindings (ドメイン固有)
- factory/
- finance/
- healthcare/
- legal/
- public_sector/

Industry bindings は空であったり、部分的であったりする場合があります。
これらは完全性ではなく、拡張ポイントを宣言するために存在します。
