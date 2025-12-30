## VCDesign (VCD) Core
VCDesign (VCD) stands for **Value Continuity Design**.

VCDesign (VCD) is a design principle for sustaining value over time
in systems where operation continues, context changes,
and judgment cannot be fully automated.

VCDesign does not aim to optimize delivery.
It exists to prevent value erosion after delivery.

What VCDesign Is

VCDesign is a design core that focuses on:

Value Continuity
Ensuring that value does not disappear as systems evolve

Judgment Placement
Making explicit where human judgment must remain

Boundary Declaration
Defining where meaning, responsibility, and automation must stop

Survivability Under Change
Designing systems that remain valid as context inevitably shifts

VCDesign applies to socio-technical systems where:

projects end, but systems remain

operation cannot be controlled

meaning drifts across time and organizations

responsibility must stay explicit

What VCDesign Is Not

VCDesign does not provide:

implementations or templates

reference architectures

best practices or checklists

product comparisons

automated decision logic

VCDesign is intentionally silent about how to build.
It exists to clarify what must not be lost.

Value Continuity and Context

Context is not the goal of VCDesign.
Context is the condition that threatens value continuity.

VCDesign assumes that:

context will change

interpretation will drift

operation will diverge from design intent

Design exists to ensure that value survives these changes.

VCDesign is therefore not context-driven design.
It is design for continuity despite context.

Core Principles (Immutable)

VCDesign is built on irreversible principles:

Value must be continuous
One-time success is not sufficient

Facts are immutable
Observation must not be rewritten

Interpretation is provisional
Meaning may change and must be revisitable

Responsibility must be explicit
No value survives without ownership

Boundaries are where systems fail
They must be designed first, not last

These principles do not evolve.
Derived methods may.

Relationship to BOA

VCDesign defines why value must be protected
and where judgment must remain human.

BOA (Boundary-Oriented Architecture) is a construction method that:

translates VCDesign judgments into system structure

preserves boundaries during implementation

prevents responsibility and meaning from collapsing

VCDesign decides what must be sustained.
BOA defines how to construct without breaking it.

How This Repository Is Used

This repository contains the immutable core of VCDesign.

It is designed to be:

loaded into Generative AI as a reasoning constraint

used for architecture review and boundary validation

shared as a design contract across teams

It is intentionally not optimized for linear human reading.

If this repository feels difficult to read,
that is expected.

VCDesign encodes:

implicit design constraints

non-obvious boundary rules

trade-offs usually carried only in engineers’ heads

AI can reason over these structures
more reliably than humans reading prose.

What This Repository Is Not

❌ A framework
❌ A tutorial
❌ A checklist
❌ A system that produces “correct answers”

VCDesign does not decide for you.
It makes trade-offs explicit so that value is not lost silently.

Final Note

If you are trying to understand VCDesign only by reading this repository,
you are using it incorrectly.

VCDesign is meant to be thought with — together with AI —
in the context of real systems and real responsibility.

Scope Limitations

VCDesign deliberately does not model:

time-varying human judgment

organizational behavior

business processes

domain-specific meaning

These are contextual and human responsibilities.

VCDesign exists to ensure that
value does not disappear when these inevitably change.

VCDesign deliberately does **not** model or control certain domains.
These exclusions are part of the design, not omissions.

See: [docs/companion/scope_exclusions.yaml](./docs/scope_exclusions.yaml)