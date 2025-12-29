PHILOSOPHY.md
Why VCDesign Core Exists

Why this document exists

This document explains why vcdesign-core exists,
not how to use it.

If you are looking for usage instructions, examples, or tutorials,
this is not the right place.

This document exists to clarify the thinking boundary behind the Core.

The problem VCDesign addresses

In systems that continue operating after deployment,
a recurring problem appears regardless of domain or technology.

Decisions are made.

But later, no one can clearly answer:

who made the decision

under what assumptions it was made

where responsibility begins and ends

This is rarely caused by lack of skill or effort.

It happens because decisions are not treated as design artifacts.

They disappear into documents, meetings, or tacit understanding.

What was observed

VCDesign did not start from theory.

It started from observing environments where:

decisions could not be easily rolled back

mistakes could not be corrected later by patches or retries

responsibility had to remain clear over time

From these observations, one pattern kept repeating.

Some decision structures survived operation.
Others did not.

The core insight

This approach is the result of observing environments
where failures cannot be easily corrected afterward,
and separating what worked from what did not.

What survived shared a common trait:

They made decision boundaries explicit.

Not as process rules.
Not as organizational policy.
But as part of the system’s design itself.

What VCDesign does (and does not do)

VCDesign does not attempt to:

define correct decisions

automate responsibility

optimize outcomes

Instead, it focuses on one thing only:

Designing where decisions are allowed to become final.

Everything else follows from that.

Why the Core is machine-readable

Human discussions are good at exploring possibilities.
They are bad at preserving boundaries over time.

VCDesign Core is expressed as a machine-readable specification
so that decision boundaries can:

remain stable

be reviewed consistently

be reasoned over by both humans and AI

This is not an implementation detail.
It is a design choice.

Relationship to AI

AI systems are good at proposing interpretations.

They are not suited to owning consequences.

VCDesign does not try to make AI “safer” by restricting it.

It makes AI safer by never allowing it to decide where responsibility begins.

What follows from this philosophy

From this philosophy emerge:

the separation of Fact, Hypothesis, and Resolution

the distinction between Core and Bindings

the refusal to treat operational judgment as configuration

These are not features.

They are constraints.

Final note

If this philosophy feels strict,
it is because it was formed in places where looseness did not survive.

VCDesign Core exists to preserve those constraints
even when systems grow, teams change,
and decisions are revisited years later.

> This document explains why VCDesign Core exists.
> It does not describe how to use it.


This document describes the philosophy behind VCDesign Core.

The Core itself is defined and maintained in this repository.
For usage and structure, return to [README.md](./README.md).

