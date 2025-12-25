# Binding: analytics_llm

This binding defines how to use **Generative AI (LLM)** inside a system while keeping
**Facts immutable**, **Interpretations provisional**, and **Responsibility explicit**.

It is intentionally domain-neutral:
- Not factory-specific
- Not SCADA/MES-specific
- Applicable to analytics, monitoring, reporting, and decision support systems

---

## Scope

### In scope
- LLM usage for:
  - summarization
  - anomaly / risk candidate generation
  - explanation drafts
  - hypothesis generation (possible causes, next questions)
  - mapping / labeling suggestions (as proposals)
  - natural language query assistance (as a router / helper)

### Out of scope
- Any direct actuation / control
- Any “automatic final decision” that changes production/business outcomes
- Any claim of factual correctness without an explicit verification boundary

---

## Non-negotiable rules

1) **LLM output is always Hypothesis**
- LLM may propose meanings, labels, causes, actions
- LLM must not finalize them as Facts

2) **Facts are immutable**
- Raw observations and recorded events are not overwritten by LLM output
- Corrections are appended as separate layers (e.g., Resolution)

3) **Responsibility cannot be delegated to the model**
- A human or an explicit system boundary owns:
  - approvals
  - notifications
  - escalation
  - external communication
  - actions that change the world

4) **Verification boundary is mandatory**
- Any “final” statement must cross a verification boundary:
  - deterministic checks
  - rule-based validation
  - human approval
  - trusted authoritative source

---

## Typical boundary placement

A safe default architecture:

- **Fact layer**: immutable logs / measurements / records
- **LLM layer**: generates Hypothesis only (drafts, candidates, explanations)
- **Resolution layer**: verification + decision ownership (human/system)
- **Action layer**: n
