# Binding: healthcare

This binding adapts VCDesign + analytics_llm to **healthcare domains**:
clinical decision support, triage assistance, care documentation, and quality/safety analysis.

Healthcare is a domain where errors may directly harm people.
This binding therefore emphasizes:

- strict separation of measurement/record (Fact) vs interpretation (Hypothesis)
- mandatory human responsibility for clinical decisions
- verification boundaries before any recommendation is treated as actionable
- traceability and safety-first behavior under uncertainty

This repository is intentionally optimized for **Generative AI-assisted design review**.
Use AI to assist reasoning and documentation—not as a clinical authority.

---

## Scope

### In scope
- LLM usage for:
  - documentation drafts (summaries, discharge note drafts)
  - differential diagnosis candidates (as Hypothesis)
  - triage question suggestions
  - guideline lookup assistance (with citations)
  - safety risk candidate generation and checklist drafts

### Out of scope
- Automated diagnosis as final Resolution
- Treatment initiation without clinician approval
- Medication ordering or dose changes without verification boundary
- Claims of certainty without evidence and provenance

---

## Healthcare-specific non-negotiable rules

1) **Clinical responsibility is human-owned**
- A licensed clinician (or explicitly responsible role) must own Resolution.

2) **Measurements and records are Facts; diagnosis is not**
- Vitals, labs, imaging, and notes are Facts as records.
- Diagnoses, causes, and treatments are Hypothesis unless verified and approved.

3) **Safety-first under uncertainty**
- If evidence is insufficient, the system must:
  - request more information, or
  - escalate to human review, or
  - choose a conservative safe path

4) **Citations and provenance are required**
- Recommendations must reference guidelines, evidence, or record sources.

---

## Typical boundary placement

- **Fact layer**
  - patient records (with access controls)
  - measurements/labs/imaging references
  - clinician notes and timestamps

- **LLM layer (Hypothesis)**
  - drafts and candidate lists
  - suggested questions and missing-info detection
  - guideline summaries with citations

- **Resolution layer**
  - clinician review
  - deterministic checks (contraindications, allergies, ranges)
  - final decisions and sign-off

- **Action layer**
  - orders, medication changes, patient-facing communication
  - only from Resolution

---

## Failure modes this binding is designed to prevent

- Hallucinated medical facts or fabricated guidelines
- Overconfident recommendations without evidence
- Patient data leakage through prompts
- Clinicians relying on AI output without audit trails
- Silent drift in clinical labels and triage logic

---

## Recommended prompts (examples)

- “Mark each statement as Fact/Hypothesis. Require citations for any clinical recommendation.”
- “Design a verification boundary for these outputs:
  which checks are deterministic, which require clinician sign-off?”
- “Identify safety risks if this system treats LLM output as Resolution.”

---

## Compatibility

See `vcdesign_binding_healthcare.yaml`.
