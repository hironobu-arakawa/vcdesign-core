# policies/

Policies define **non-negotiable decision boundaries**.

They are evaluated when:
- automated optimization is proposed
- AI-generated actions are reviewed
- trade-offs between values are requested

Policies are not guidelines.
Policies are not best practices.
Policies exist to **deny, stop, or require explicit responsibility**.

---

## boundary-lexicographic-policy

This policy enforces a lexicographic order of boundaries:

SAFETY > COMPLIANCE > TRUST > ETHICS > BUSINESS_VIABILITY > KPI_EFFICIENCY

Lower-level improvements must never violate higher-level boundaries.

- `.md` : human-readable justification
- `.json` : canonical machine-readable policy
- `.rego` : executable enforcement logic
