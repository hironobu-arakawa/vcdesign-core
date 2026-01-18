# bindings/

Bindings define how VCDesign Core is applied to specific contexts.

They are not implementations.
They are not specifications.
They are not examples.

Bindings describe:
- which constraints remain invariant
- which assumptions change
- where responsibility and verification are placed

---

## Binding categories

### Capability / Technology bindings
- analytics_llm/
  - Using LLMs while preserving Fact / Meaning / Responsibility separation

### Organizational / Governance bindings
- enterprise_decision/
  - Applying VCDesign to enterprise-level decision processes

### Industry bindings (domain-specific)
- factory/
- finance/
- healthcare/
- legal/
- public_sector/

Industry bindings may be empty or partial.
They exist to declare extension points, not completeness.
