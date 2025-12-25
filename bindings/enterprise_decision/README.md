# Binding: enterprise_decision

This binding adapts VCDesign + analytics_llm to **enterprise-level decision making**:
strategy, investment planning, portfolio management, organizational design, and executive reviews.

Enterprise decisions are characterized by:
- high ambiguity
- long-lasting consequences
- limited reversibility
- collective responsibility

This binding focuses on making **decision boundaries explicit**,
so that Generative AI can assist reasoning **without owning outcomes**.

This repository is intentionally optimized for **Generative AI-assisted design review**,
not for automated decision making.

---

## Scope

### In scope
- LLM usage for:
  - option generation and comparison (as candidates)
  - scenario drafting and impact analysis (as Hypothesis)
  - risk and assumption surfacing
  - summary drafts for executive review
  - question generation to expose blind spots
  - consistency checks across documents and plans

### Out of scope
- Automatic approval or rejection of strategic options
- Autonomous budget allocation or investment execution
- “Best decision” claims without explicit ownership
- Treating AI output as the decision record itself

---

## Enterprise-specific non-negotiable rules

1) **Decisions are not data**
- KPIs, results, contracts, and records can be Facts.
- Strategic direction, priorities, and choices are not Facts.

2) **AI proposes; humans decide**
- LLM may generate options and reasoning drafts.
- Resolution must be owned by an explicit decision body or role.

3) **Irreversibility must be acknowledged**
- Decisions with long-term impact require:
  - explicit assumptions
  - risk acknowledgment
  - named responsibility

4) **Decision trails matter**
- It must be possible to answer:
  - what was decided
  - based on which evidence
  - under which assumptions
  - by whom and when

---

## Typical boundary placement

- **Fact layer**
  - historical performance metrics
  - financial results and contracts
  - validated reports and records
  - external factual inputs (market data as records)

- **LLM layer (Hypothesis)**
  - strategic options
  - scenario narratives
  - impact and risk candidates
  - assumption lists and open questions

- **Resolution layer**
  - executive or committee decision
  - assumption acceptance or rejection
  - prioritization and commitment logging

- **Action layer**
  - execution programs
  - budget allocation
  - organizational changes
  - only from Resolution

---

## Failure modes this binding is designed to prevent

- Treating persuasive narratives as evidence
- Overconfidence driven by fluent AI explanations
- Decisions made without explicit ownership
- Loss of context (“why we chose this”)
- Silent drift of assumptions over time
- Retroactive rationalization without records

---

## Recommended prompts (examples)

- “List options as Hypothesis only.
  For each, identify assumptions, risks, and missing evidence.”

- “Review this strategy document using VCDesign + enterprise_decision binding.
  Identify where interpretation is treated as Fact.”

- “Design a decision log schema:
  what must be recorded at Resolution time to preserve accountability?”

---

## When NOT to use an LLM

- When decisions are time-critical and evidence is incomplete
- When responsibility cannot be clearly assigned
- When persuasion risk outweighs analytical benefit
- When the organization is not prepared to record decision rationale

---

## Compatibility

This binding extends `analytics_llm` and assumes VCDesign core principles.
See `vcdesign_binding_enterprise_decision.yaml`.
