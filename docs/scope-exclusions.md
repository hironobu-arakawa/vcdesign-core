# Scope Exclusions  
VCDesign / BOA Companion  
Boundary-Oriented Architecture — What It Does *Not* Model

This document defines the **explicit non-scope** of VCDesign and BOA.

VCDesign is a boundary-oriented architectural specification.
It defines **what must remain stable**, **what must remain separate**,  
and **where responsibility must stay human**.

Equally important is clarifying **what VCDesign does *not* attempt to model**.  
These exclusions prevent misuse, overreach, and false expectations.

This document is part of the Companion set.  
It supplements the Core but does not modify it.

---

# 1. Temporal Dynamics  
### VCDesign does **not** model time-varying human judgment, meaning, or responsibility.

Meaning and responsibility evolve with context, experience, and operational reality.  
These changes cannot be fully captured by any static specification.

VCDesign handles:

- ✔ Fact time-series (e.g., sensor values, logs)

VCDesign does **not** handle:

- ✖ Meaning drift over time  
- ✖ Shifts in human judgment  
- ✖ Operational exceptions or emergent behavior  
- ✖ Contextual reinterpretation of events  

**Principle:**  
Fact の時間変化のみを扱い、Meaning / Responsibility の変化は人間の領域とする。  
これは、時間による意味や判断の変化をシステムが完全に扱うことは不可能であり、  
越権や誤解を防ぐためである.

---

# 2. Organizational Structure  
### VCDesign does **not** define organizational charts, authority hierarchies, or governance models.

Organizations change faster than systems.  
Embedding organizational structure into architecture creates brittle designs.

VCDesign handles:

- ✔ Responsibility assignment boundaries  
- ✔ Where decisions become final  

VCDesign does **not** handle:

- ✖ Organizational hierarchy  
- ✖ Approval chains  
- ✖ Cultural norms  
- ✖ Team structure or reporting lines  

These belong to **Context**, not architecture.

---

# 3. Value Judgement and Ethics  
### VCDesign does **not** define what is “good,” “correct,” or “ethical.”

Value judgments are inherently human.  
VCDesign only defines **where** decisions occur, not **what** decisions should be.

VCDesign handles:

- ✔ Decision structure  
- ✔ Responsibility boundaries  

VCDesign does **not** handle:

- ✖ Ethical evaluation  
- ✖ Moral correctness  
- ✖ Organizational values  
- ✖ Trade-off preferences  

These remain human responsibilities.

---

# 4. Business Processes  
### VCDesign does **not** define workflows, SOPs, or operational procedures.

Business processes are domain- and organization-specific.  
They evolve with practice, regulation, and local knowledge.

VCDesign handles:

- ✔ Structural dependencies  
- ✔ Where interpretation enters the system  

VCDesign does **not** handle:

- ✖ Process flows  
- ✖ Step-by-step procedures  
- ✖ SOPs  
- ✖ Operational rules  

These belong to Meaning and Responsibility, not architecture.

---

# 5. Domain-Specific Semantics  
### VCDesign does **not** define the meaning of domain concepts.

VCDesign is domain-agnostic by design.  
Domain semantics belong in **Bindings**, not in the Core or Companion.

VCDesign handles:

- ✔ Meaning structure (Fact → Interpretation → Resolution)

VCDesign does **not** handle:

- ✖ Factory-specific terminology  
- ✖ Medical or financial semantics  
- ✖ Domain-specific thresholds or rules  

Bindings extend the Core for each domain.

---

# 6. AI Model Internals  
### VCDesign does **not** define how AI models work internally.

VCDesign governs **how AI participates in decision structures**,  
not how AI is built.

VCDesign handles:

- ✔ AI-generated interpretations as Meaning  
- ✔ Boundaries preventing AI from owning consequences  

VCDesign does **not** handle:

- ✖ Model architecture  
- ✖ Training methods  
- ✖ Parameters  
- ✖ Inference algorithms  

These are implementation details outside the architectural boundary.

---

# Summary Table

| Area | VCDesign Handles | VCDesign Does *Not* Handle |
|------|------------------|----------------------------|
| Time | Fact time-series | Meaning/Responsibility evolution |
| Organization | Responsibility boundaries | Org charts, authority, governance |
| Values | Decision structure | Ethics, correctness, preferences |
| Processes | Structural dependencies | Workflows, SOPs, procedures |
| Semantics | Meaning structure | Domain-specific meaning |
| AI | Interpretation boundaries | Model internals |

---

# Why these exclusions matter

These exclusions exist to:

- prevent overreach  
- avoid false expectations  
- keep the Core stable  
- preserve human responsibility  
- maintain boundary clarity  
- ensure VCDesign remains domain-agnostic  

VCDesign is powerful precisely because it **does not** attempt to model everything.

It defines **where decisions become final**,  
not **what decisions should be**.

---

# Relationship to the Core

This document:

- does **not** modify the Core  
- does **not** extend the Core  
- does **not** override any Core principle  

It clarifies the **outer boundary** of VCDesign and BOA,  
so that both humans and AI can use the Core safely and correctly.

For the Core specification, see:  
`vcdesign-core/vcdesign_core.yaml`

For philosophical background, see:  
`PHILOSOPHY.md`

