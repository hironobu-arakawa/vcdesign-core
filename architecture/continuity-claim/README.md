# architecture/

This folder contains **architectural claims**, not specifications.

Architectural claims define:
- what must hold true structurally
- regardless of implementation, domain, or tooling

They are not optimized, extended, or layered.
They exist as invariant constraints.

---

## continuity-claim.md

Defines the **minimum condition for connection** in VCDesign.

- Connection is based on *Value Continuity*, not compatibility
- Silence is treated as a safety signal
- This claim precedes APIs, schemas, and implementations

There is intentionally only one document here.
