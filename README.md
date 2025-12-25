VCDesign Core

Boundary-Oriented Design Specification for Human × AI Co-Design

What this repository is

This repository contains VCDesign (Value-Context Design) —
a machine-readable architectural specification for designing systems across unstable boundaries such as:

Operation × Design

OT × IT

Fact × Interpretation

Responsibility × Automation

It is not optimized for human reading first.

Instead, this repository is designed to be:

Loaded into Generative AI and used as a reasoning substrate
for architecture review, design assistance, and boundary validation.

This repository is intentionally difficult to read

If you feel this repository is hard to understand by simply reading it,
that is expected and intentional.

VCDesign encodes:

implicit design constraints

non-obvious boundary rules

trade-offs that are usually carried only in engineers’ heads

These are hard to express linearly in prose, but easy for AI to reason over once structured.

👉 This repository is optimized for AI cognition, not human cognition.

Primary usage (recommended)
✔ Use with Generative AI

Typical usage:

Load this repository into a Generative AI (LLM)

Ask the AI to:

review an architecture

detect boundary violations

explain trade-offs

suggest safer design alternatives

Use the AI’s output as a design review partner, not as an oracle

Example prompts:

“Review this system design using VCDesign principles.”

“Where does this architecture mix Fact and Interpretation?”

“Which boundaries are likely to break during operation?”

Secondary usage (advanced)

As a design contract shared across teams

As a reference spec for internal design reviews

As a constraint set for custom LLM tooling

As a foundation for domain-specific bindings (factory, SCADA, MES, etc.)

Repository structure
vcdesign-core/
  vcdesign_core.yaml        # Core architectural specification (immutable principles)
  bindings/
    factory/
      vcdesign_binding_factory.yaml
  docs/
  examples/

vcdesign_core.yaml

The core specification:

universal principles

boundary definitions

responsibility separation

quality and observability assumptions

This file should remain stable and conservative.

bindings/

Bindings are contextual profiles that connect the Core to real domains.

They:

extend the Core without overriding it

encode domain constraints and operational realities

are expected to evolve over time

What this repository is NOT

❌ A framework

❌ A reference implementation

❌ A tutorial

❌ A checklist

❌ A system that produces “correct answers”

VCDesign does not decide for you.
It makes trade-offs explicit.

Design philosophy (short)

Facts are immutable

Interpretation is provisional

Responsibility must be explicit

Boundaries are where systems fail — design them first

AI may propose meaning, but must not own consequences

Why YAML?

YAML is used intentionally because it is:

readable enough for humans

structured enough for machines

stable across time

easy to diff, version, and reason over

VCDesign treats YAML not as configuration,
but as an architectural language.

License

MIT License — free to use, adapt, and embed.
Attribution appreciated but not required.

Final note

If you are trying to “understand everything” by reading this repository alone,
you are using it incorrectly.

VCDesign is meant to be thought with — together with AI.