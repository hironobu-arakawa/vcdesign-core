# Binding: legal

This binding adapts VCDesign + analytics_llm to **legal domains**:
contracts, compliance, internal policy, litigation support, and governance.

Legal work is primarily about **interpretation under constraints**.
This binding therefore emphasizes:

- strict separation of Fact vs Interpretation
- explicit verification boundaries for claims
- clear responsibility ownership for advice and decisions
- auditability of “who decided what, based on which evidence”

This repository is intentionally optimized for **Generative AI-assisted design review**.
Use AI to structure reasoning—not as an authority.

---

## Scope

### In scope
- LLM usage for:
  - issue spotting and risk candidate generation
  - clause comparison and diff summaries
  - argument outline drafts (as proposals)
  - policy-to-control mapping drafts
  - evidence indexing and retrieval assistance
  - question generation for human reviewers

### Out of scope
- “Final legal advice” without explicit human responsibility
- Automatic contract acceptance/termination
- Automatic external legal communications
- Treating model output as evidence or authoritative interpretation

---

## Legal-specific non-negotiable rules

1) **Textual sources are Facts; interpretations are not**
- Contract texts, laws, regulations, court decisions, and signed records can be Fact (as documents).
- Any statement about meaning, enforceability, or outcome is Interpretation (Hypothesis) unless verified.

2) **Citations are mandatory**
- Any claim must cite:
  - document references (IDs/versions)
  - relevant clauses/sections
  - timestamped sources

3) **Authority is owned by humans**
- The model may draft, compare, and propose.
- Responsibility for advice and decisions stays with a named role (legal counsel / responsible owner).

4) **Change detection matters**
- Legal texts change. Interpretations drift.
- Resolution must include:
  - versioning
  - effective dates
  - jurisdiction scope

---

## Typical boundary placement

- **Fact layer**
  - signed documents and versions
  - primary sources and their versions
  - evidence logs and provenance

- **LLM layer (Hypothesis)**
  - interpretation drafts
  - risk candidate lists
  - clause mapping proposals
  - structured questions for review

- **Resolution layer**
  - human legal review
  - citation verification
  - jurisdiction and date validity checks
  - final advice classification and ownership

- **Action layer**
  - approvals, notices, filings, policy updates
  - only from Resolution

---

## Failure modes this binding is designed to prevent

- Hallucinated citations and fabricated authorities
- Mixing “what the document says” with “what it means”
- Outdated versions silently used for decisions
- Responsibility diffusion (“the AI said it was fine”)
- Non-auditable advice trails

---

## Recommended prompts (examples)

- “Separate Fact vs Interpretation for this legal memo.
  Mark every sentence as Fact/Hypothesis and require citations for Facts.”

- “Review this contract workflow using VCDesign + legal binding.
  Identify any place where interpretation could be treated as Fact.”

- “Propose a verification boundary:
  which checks are deterministic, and which require human legal review?”

---

## Compatibility

See `vcdesign_binding_legal.yaml`.
