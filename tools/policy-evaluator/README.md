# policy-evaluator (reference)

This tool is a **reference evaluator** for VCDesign boundary policies.

It evaluates an Optimization Proposal against a lexicographic boundary policy and returns:
- decision: ALLOW / REVIEW / DENY
- violations: matched rules (boundary + rule_id + severity + message)
- required_approvals: approvals needed for soft boundaries

> Note: This is **not** the VCDesign standard itself.  
> It is a minimal runnable reference used for validation, demos, and CI.

---

## Files

- `evaluator.py`  
  Core evaluation engine (dependency-free).
- `run_all.py`  
  Runs evaluation for all example proposals and prints a summary.
- `expectations.json`  
  Optional expected outcomes for CI-style checks.

---

## Inputs

- Policy file (recommended): `policies/boundary-lexicographic-policy.json`
- Proposal files: `examples/proposal*.json`

---

## Usage

From repository root:

### 1) Evaluate a single proposal

```bash
python tools/policy-evaluator/evaluator.py \
  --policy policies/boundary-lexicographic-policy.json \
  --proposal examples/proposal_deny_safety.json
2) Run all proposals (summary)
bash
コードをコピーする
python tools/policy-evaluator/run_all.py \
  --policy policies/boundary-lexicographic-policy.json \
  --examples-dir examples \
  --pattern "proposal*.json"
3) Run all proposals with expectations (CI mode)
bash
コードをコピーする
python tools/policy-evaluator/run_all.py \
  --policy policies/boundary-lexicographic-policy.json \
  --expect-map tools/policy-evaluator/expectations.json
If the actual decision differs from the expected one, the process exits with code 3.

Output (example)
json
コードをコピーする
{
  "decision": "DENY",
  "violations": [
    {
      "boundary": "SAFETY",
      "rule_id": "safety.no_margin_reduction",
      "severity": "critical",
      "message": "Safety margin reduced or incident risk increased."
    }
  ],
  "required_approvals": []
}
Notes
Policy format
evaluator.py loads the policy as JSON-compatible YAML (YAML subset).
To keep dependencies at zero, the recommended policy format is JSON:

✅ policies/boundary-lexicographic-policy.json

If you prefer full YAML syntax, you can:

convert YAML to JSON in CI (recommended), or

add PyYAML and update the loader in evaluator.py.

Scope
This evaluator implements:

Lexicographic boundary order (hard stops)

Soft boundary review/approval

Structured output for audits

It intentionally does not implement:

Organizational approval routing (RBAC)

Policy signing / attestation

Runtime enforcement hooks

Those belong to bindings/ or downstream system integrations.