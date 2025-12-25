# Binding: finance

This binding adapts VCDesign + analytics_llm to **finance domains**:
trading, treasury, accounting, risk, credit, fraud detection, compliance.

Finance is a domain where **small errors can become irreversible actions**.
This binding therefore emphasizes:

- immutable facts (books/ledger/transactions)
- explicit verification boundaries
- responsibility ownership (human/system)
- auditability and reproducibility

This repository is intentionally optimized for **Generative AI-assisted design review**.
Use AI to reason over boundary placement and failure modes—never as an authority.

---

## Scope

### In scope
- Decision support for:
  - risk assessment drafts
  - anomaly/fraud candidate generation
  - reconciliation assistance
  - compliance checklist drafts
  - policy-to-control mapping (as proposals)
  - report summarization with evidence pointers
- Natural language interfaces that **generate queries** (with guardrails)
- LLM-based explanation drafts that reference immutable records

### Out of scope
- Any autonomous execution of:
  - orders / trades
  - payments / fund transfers
  - credit approvals
  - external disclosures
- “Final” statements without a verification boundary
- Overwriting authoritative financial records

---

## Finance-specific non-negotiable rules

1) **Ledger/Book is the authority (Fact)**
- The ledger, confirmed transactions, and signed documents are the source of truth.
- AI outputs must never replace them.

2) **Predictions are not facts**
- Market outlook, risk estimates, and “probable causes” are Hypothesis only.

3) **Execution boundary must be explicit**
- Any action that moves money or changes positions must require:
  - deterministic validation, and
  - explicit ownership (human/system), and
  - auditable approval (where applicable)

4) **Auditability is mandatory**
- Every Resolution must cite:
  - evidence references (transaction IDs, document IDs, timestamps)
  - verification method used
  - responsible owner

---

## Typical boundary placement

A safe default architecture:

- **Fact layer**
  - immutable transactions (append-only)
  - ledger/book entries (authoritative)
  - signed documents / confirmations
  - event logs (who did what, when)

- **LLM layer (Hypothesis)**
  - drafts: explanations, summaries, candidate anomalies
  - proposals: risk drivers, likely mismatches, next checks
  - query drafting (with strict constraints)

- **Resolution layer**
  - deterministic checks (reconciliation rules, thresholds, policy rules)
  - human approvals for high-impact actions
  - final classification and decision logging

- **Action layer**
  - payments, trades, disclosures, alerts
  - only triggered from Resolution

---

## Failure modes this binding is designed to prevent

- AI-generated narratives being mistaken as evidence
- “Confidence-sounding” text triggering trades or payments
- Summaries becoming the only record of truth
- Responsibility diffusion (“the model said so”)
- Silent semantic drift changing risk labels over time
- Data leakage via prompts (PII / confidential trading intent)

---

## Recommended prompts (examples)

### Architecture review
- “Review this finance workflow using VCDesign + finance binding.
  Identify any paths where Hypothesis could trigger execution.”

### Output contract
- “For each output type, define:
  Fact inputs, Hypothesis outputs, verification boundary, and the owner.”

### Guardrails for NL query assistant
- “Design a safe NL-to-SQL interface:
  list allowed tables/fields, disallowed operations, and required logging.”

---

## When NOT to use an LLM in finance

- When deterministic rules fully cover the task
- When verification cannot be enforced
- When actions are irreversible and containment is weak
- When confidentiality cannot be protected in prompt flows

---

## Compatibility

This binding extends `analytics_llm` and assumes VCDesign core principles.
See `vcdesign_binding_finance.yaml`.
