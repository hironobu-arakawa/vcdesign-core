# Scope Exclusions  
# VCD (Philosophy) & BOA (Architecture) Companion  
# What VCDesign Does *Not* Model

This document defines the **explicit non-scope** of the Value Continuity Design (VCD) ecosystem.

VCD is a philosophical core defining **why boundaries must exist**.
BOA is the architectural layer defining **how to construct them**.

Equally important is clarifying **what the ecosystem does *not* attempt to model**.  
These exclusions prevent misuse, overreach, and false expectations.

---

# 1. Temporal Dynamics  
### VCD does **not** model time-varying human judgment.

Meaning and responsibility evolve with context, experience, and operational reality.  
These changes cannot be fully captured by any static specification.

VCD handles:
- ✔ Fact time-series (e.g., sensor values, logs)
- ✔ Versioning of Interpretation

VCD does **not** handle:
- ✖ Meaning drift over time  
- ✖ Shifts in human judgment  
- ✖ Operational exceptions or emergent behavior  

**Principle:**  
Fact の時間変化のみを扱い、Meaning / Responsibility の変化は人間の領域とする。

---

# 2. Organizational Structure  
### VCD does **not** define organizational charts or governance models.

Organizations change faster than systems.  
Embedding organizational structure into architecture creates brittle designs.

VCD handles:
- ✔ Responsibility assignment boundaries (Who owns what *role*)

VCD does **not** handle:
- ✖ Organizational hierarchy  
- ✖ Approval chains  
- ✖ Team structure  

These belong to **Context**, not philosophy or architecture.

---

# 3. Value Judgement and Ethics  
### VCD does **not** define what is “good” or “correct.”

Value judgments are inherently human.  
VCD only defines **where** decisions occur, not **what** decisions should be.

VCD handles:
- ✔ Decision structure (Resolution)

VCD does **not** handle:
- ✖ Ethical evaluation  
- ✖ Moral correctness  
- ✖ Trade-off preferences  

---

# 4. Business Processes  
### VCD does **not** define workflows or SOPs.

Business processes are domain- and organization-specific.

VCD handles:
- ✔ Structural dependencies (Fact → Interpretation)

VCD does **not** handle:
- ✖ Process flows  
- ✖ Step-by-step procedures  
- ✖ SOPs  

These belong to the IDG (Implementation) layer or external context.

---

# 5. Domain-Specific Semantics  
### VCD does **not** define the meaning of domain concepts.

VCD is domain-agnostic by design.  
Domain semantics belong in **Bindings**.

VCD handles:
- ✔ Meaning structure (Fact / Interpretation / Resolution)

VCD does **not** handle:
- ✖ Domain-specific terminology (e.g., "Trade", "Diagnosis")
- ✖ Domain-specific thresholds  

Bindings extend the Core for each domain.

---

# 6. AI Model Internals  
### VCD does **not** define how AI models work internally.

VCD governs **how AI participates in decision structures**, not how AI is built.

VCD handles:
- ✔ AI-generated interpretations as Meaning (Hypothesis)
- ✔ Boundaries preventing AI from owning consequences

VCD does **not** handle:
- ✖ Model architecture  
- ✖ Training methods  
- ✖ Inference algorithms  

---

# Summary Table

| Area | VCD Handles | VCD Does *Not* Handle |
|------|-------------|-----------------------|
| Time | Fact continuity, Versioning | Meaning evolution |
| Organization | Responsibility boundaries | Org charts, governance |
| Values | Decision structure | Ethics, preferences |
| Processes | Structural dependencies | Workflows, SOPs |
| Semantics | Meaning structure | Domain meaning |
| AI | Hypothesis boundaries | Model internals |

---

# Relationship to the Core

This document clarifies the **outer boundary** of the VCD ecosystem.

For the Philosophical Core, see:  
`vcdesign_core.yaml`

For Architecture, refer to the BOA repository.
