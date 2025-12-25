# Binding: public_sector

This binding adapts VCDesign + analytics_llm to **public sector decision making**:
government, municipalities, public agencies, regulators, and public infrastructure governance.

Public-sector decisions are defined by:
- strong accountability to society
- transparency requirements
- procedural legitimacy
- collective and distributed responsibility
- long-term impact on citizens

This binding focuses on ensuring that Generative AI:
- assists reasoning and documentation
- never replaces democratic or procedural decision-making
- never obscures responsibility or rationale

This repository is intentionally optimized for
**Generative AI-assisted design review**, not automated governance.

---

## Scope

### In scope
- LLM usage for:
  - policy option drafting (as candidates)
  - impact and trade-off summaries
  - stakeholder perspective surfacing
  - risk and unintended consequence identification
  - public document summarization with references
  - question generation for deliberation bodies

### Out of scope
- Autonomous policy decisions
- Automatic approval or rejection of public actions
- Direct citizen-facing decisions without human oversight
- Treating AI output as official policy or record

---

## Public-sector non-negotiable rules

1) **Legitimacy matters as much as correctness**
- Decisions must follow defined procedures.
- AI output cannot substitute for process legitimacy.

2) **Public records are authoritative Facts**
- Laws, regulations, official statistics, meeting minutes, and published records are Facts as records.
- Policy interpretations and recommendations are Hypothesis.

3) **Collective responsibility must be explicit**
- Decisions are often made by bodies, not individuals.
- Resolution must clearly identify:
  - the decision body
  - the procedure followed
  - the scope of authority

4) **Explainability to third parties is mandatory**
- It must be possible to explain decisions to:
  - citizens
  - auditors
  - courts
  - oversight bodies

---

## Typical boundary placement

- **Fact layer**
  - laws and regulations
  - official statistics and reports
  - public records and minutes
  - published budgets and plans

- **LLM layer (Hypothesis)**
  - policy option drafts
  - impact and risk candidates
  - comparative summaries
  - stakeholder impact narratives

- **Resolution layer**
  - formal deliberation and approval
  - procedural validation
  - responsibility attribution to a body
  - decision record publication

- **Action layer**
  - policy execution
  - public programs
  - regulatory enforcement
  - only from Resolution

---

## Failure modes this binding is designed to prevent

- AI-generated narratives being mistaken for official policy
- Hidden influence on public decisions without disclosure
- Responsibility dilution across committees
- Decisions that cannot be explained after the fact
- Procedural shortcuts justified by AI efficiency
- Loss of trust due to opaque reasoning

---

## Recommended prompts (examples)

- “List policy options as Hypothesis only.
  For each, identify benefits, risks, stakeholders, and uncertainties.”

- “Review this decision process using VCDesign + public_sector binding.
  Identify where legitimacy or transparency could be compromised.”

- “Design a decision record template that enables third-party explanation
  without exposing sensitive deliberation details.”

---

## When NOT to use an LLM

- When procedural neutrality cannot be ensured
- When outputs cannot be disclosed or explained
- When time pressure undermines deliberative process
- When the decision is legally required to be human-only

---

## Compatibility

This binding extends `analytics_llm` and assumes VCDesign core principles.
See `vcdesign_binding_public_sector.yaml`.
