# VCDesign Glossary

This glossary defines **canonical meanings and status** of terms used in VCDesign.

It is:
- NOT a tutorial
- NOT a philosophical explanation
- A reference anchor to prevent semantic drift

Narrative documents may use these terms freely without explanation.

# VCDesign Glossary

This glossary defines **canonical meanings and status** of terms used in VCDesign.

It is:
- NOT a tutorial
- NOT a philosophical explanation
- A reference anchor to prevent semantic drift

Narrative documents may use these terms freely without explanation.

---

## Core Concepts

### Value Continuity
**Status:** Canonical  
**Language:** English (primary) / Japanese (secondary)

**Definition:**  
The ability of a system to preserve its intended value across time, change, and optimization pressure.

**Narrative Role:**  
The core concern VCDesign is designed to protect.

**Notes:**  
- Value may survive even when implementations are replaced  
- Continuity is observed over time, not guaranteed at a single point

**Do not confuse with:**  
- System stability  
- Uptime or availability  

---

### Value Continuity Design (VCDesign)
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A design discipline focused on preserving value continuity under constant change and optimization pressure.

**Narrative Role:**  
The framework that organizes all concepts in this repository family.

**Notes:**  
- Not a methodology  
- Not limited to software systems

---

### Chapter
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A bounded phase in which value continuity is evaluated under specific assumptions.

**Narrative Role:**  
Explains why systems must be judged relative to time and context.

**Notes:**  
- Chapters end even if systems continue  
- Design decisions are chapter-dependent

---

### Continuer
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A role responsible for preserving value continuity across chapters.

**Narrative Role:**  
The implicit protagonist of VCDesign narratives.

**Notes:**  
- Not necessarily the original creator  
- Often appears during transition or crisis

---

### Value Break
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A moment where intended value can no longer be preserved under existing structure.

**Narrative Role:**  
Triggers redesign, rollback, or responsibility reassignment.

---

### Structural Debt
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
Accumulated constraints that prevent value continuity, even if the system still functions.

**Narrative Role:**  
Explains why “working systems” still fail over time.

---

## Optimization Pressure

### Constant High-Speed Optimization
**Status:** Canonical  
**Language:** English (primary) / Japanese (secondary)

**Definition:**  
A precondition of modern system environments that constantly demands high-speed improvement and optimization.  
It refers to the structural pressure continuously applied to designers and operators, rather than individual technical choices.

**Narrative Role:**  
The background condition from which VCDesign emerges.

**Notes:**  
- Does not imply good or evil  
- Applies equally to humans, AI, and organizations

**Do not confuse with:**  
- Agile Development  
- Performance Optimization  

---

## Boundary & Responsibility

### Responsibility
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
The obligation to bear the consequences of a decision.

**Narrative Role:**  
Separates decision authority from execution.

---

### Responsibility Pool
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A conceptual space where undecidable or deferred responsibility is temporarily held.

**Narrative Role:**  
Prevents forced or premature decisions.

---

### responsibility-pools
**Status:** Canonical  
**Language:** English (primary) / Japanese (secondary needed)

**Definition:**  
Structured responsibility pools that retain undecidable responsibility until a legitimate decision-maker can assume it.

**Narrative Role:**  
Enables judgment suspension without value loss.

**Notes:**  
- Foundational to Resolution Protocol  
- Can be visualized via idk-lamp

---

### Responsibility Closure
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
The act of explicitly assigning responsibility and closing a responsibility pool.

**Narrative Role:**  
Marks the transition from suspension to action.

---

### Decision Stop
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
An explicit halt of decision-making due to insufficient determinability.

**Narrative Role:**  
Protects humans from silent AI overreach.

---

## Architecture & Mechanisms

### Boundary
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A designed separation that constrains meaning, responsibility, or action.

**Narrative Role:**  
The fundamental unit of safety in VCDesign.

---

### BOA (Boundary-Oriented Architecture)
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
An architectural approach that prioritizes explicit boundary definition over component structure.

**Narrative Role:**  
Structural realization of VCDesign principles.

---

### IDG (Interface-Determinability Gate)
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A gate that evaluates whether sufficient information exists to allow a decision.

**Narrative Role:**  
Prevents decisions under false certainty.

---

### RP (Resolution Protocol)
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A protocol that governs how unresolved responsibility is handled, escalated, or returned.

**Narrative Role:**  
Ensures responsibility is never silently dropped.

---

### idk-lamp / I Don’t Know Signal
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A deliberately designed signal indicating that a system must stop deciding and defer to human responsibility.

**Narrative Role:**  
Makes uncertainty visible and actionable.

---

## Design Attitudes

### Design Premised on Recreation
**Status:** Canonical  
**Language:** English (primary)

**Definition:**  
A design attitude that assumes future recreation and preserves the boundaries of value, responsibility, and judgment.

**Narrative Role:**  
Shifts focus from code preservation to value preservation.

**Do not confuse with:**  
- Disposable Development  
- Acceptance of Technical Debt  

---

### Continuity Claim Protocol
**Status:** Provisional  
**Language:** English only (JP needed)

**Definition:**  
A protocol that declares which aspects of value are claimed to be preserved across system change.

**Narrative Role:**  
Connects abstract value continuity to explicit claims.

**Notes:**  
- Not yet part of VCDesign core  
- Relationship with RP / IDG under exploration

---

## Meta / Ambiguous Terms

### Design
**Status:** Working Term  
**Language:** English (primary)

**Definition:**  
The act of deciding what must not change before deciding what may change.

---

### Optimization
**Status:** Working Term  
**Language:** English (primary)

**Definition:**  
Local improvement that may conflict with long-term value continuity.

---

### Safety
**Status:** Working Term  
**Language:** English (primary)

**Definition:**  
The condition where irreversible harm is structurally prevented, not statistically unlikely.

---

### Failure
**Status:** Working Term  
**Language:** English (primary)

**Definition:**  
Loss of value continuity, regardless of system operability.

---

## About Language Usage in This Glossary

In this glossary, the Japanese and English versions are **not translations** of each other.

- Each language version is an **independent definition set**
  optimized for its own design, thinking, and discussion context
- Exact semantic equivalence is not guaranteed
- Terms may correspond across languages, but they are not "translations"

In VCDesign, language is treated not merely as a medium of expression,
but as **part of the design boundary itself**.

Accordingly:
- English definitions tend to emphasize structure, protocol, and abstraction
- Japanese definitions tend to emphasize design attitude, context, and lived understanding
