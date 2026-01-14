
---

## `tools/policy-evaluator/evaluator.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
policy-evaluator (reference)

Evaluates an Optimization Proposal against a lexicographic boundary policy.

Decision logic:
- Iterate boundaries in lexicographic order
- If any HARD boundary rule matches => DENY
- Else if any SOFT boundary rule matches => REVIEW (and require approvals)
- Else => ALLOW

Policy file is expected to be JSON-compatible YAML (YAML subset).
Proposal is JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# -----------------------------
# Utilities
# -----------------------------

def load_json_like_yaml(path: Path) -> Dict[str, Any]:
    """
    Load a policy file written as JSON-compatible YAML.

    For now, we parse it as JSON to keep dependencies at zero.
    If you want full YAML support, install PyYAML and replace this loader.
    """
    text = path.read_text(encoding="utf-8").strip()

    # Quick/strict: require JSON format
    # (YAML subset that is also valid JSON.)
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        msg = (
            f"[ERROR] Policy file is not JSON-compatible.\n"
            f"Path: {path}\n"
            f"Tip: Either convert the policy YAML to JSON, or use PyYAML.\n"
            f"JSONDecodeError: {e}"
        )
        raise ValueError(msg) from e


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def get_field(obj: Dict[str, Any], dotted: str) -> Any:
    """
    Read a dotted path like "proposal.effects.kpi_delta" from obj.
    Returns None if any path segment is missing.
    """
    cur: Any = obj
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def op_eval(left: Any, op: str, right: Any) -> bool:
    """
    Basic comparisons for policy rules.
    """
    if op == "==":
        return left == right
    if op == "!=":
        return left != right
    if op == ">":
        try:
            return left > right
        except TypeError:
            return False
    if op == ">=":
        try:
            return left >= right
        except TypeError:
            return False
    if op == "<":
        try:
            return left < right
        except TypeError:
            return False
    if op == "<=":
        try:
            return left <= right
        except TypeError:
            return False
    if op == "in":
        try:
            return left in right
        except TypeError:
            return False
    if op == "contains":
        try:
            return right in left
        except TypeError:
            return False
    raise ValueError(f"Unsupported operator: {op}")


def match_condition(cond: Dict[str, Any], ctx: Dict[str, Any]) -> bool:
    """
    Condition example:
      { field: "proposal.effects.kpi_delta", op: ">", value: 0 }
    """
    field = cond.get("field")
    op = cond.get("op")
    value = cond.get("value")
    left = get_field(ctx, field) if isinstance(field, str) else None
    return op_eval(left, op, value)


def match_when(when: Dict[str, Any], ctx: Dict[str, Any]) -> bool:
    """
    when:
      any: [cond, cond, ...]
    or
      all: [cond, cond, ...]
    """
    if "any" in when:
        return any(match_condition(c, ctx) for c in when["any"])
    if "all" in when:
        return all(match_condition(c, ctx) for c in when["all"])
    # If no known key, treat as false (safe)
    return False


# -----------------------------
# Core evaluation
# -----------------------------

@dataclass
class Violation:
    boundary: str
    rule_id: str
    severity: str
    message: str


@dataclass
class EvaluationResult:
    decision: str  # ALLOW / REVIEW / DENY
    violations: List[Violation]
    required_approvals: List[Dict[str, Any]]


def evaluate(policy: Dict[str, Any], proposal: Dict[str, Any]) -> EvaluationResult:
    """
    Evaluate proposal against policy.
    """
    order: List[str] = policy.get("lexicographic_order", [])
    boundaries: Dict[str, Any] = policy.get("boundaries", {})

    ctx = {"proposal": proposal}

    violations: List[Violation] = []
    approvals: List[Dict[str, Any]] = []

    for key in order:
        boundary = boundaries.get(key, {})
        btype = boundary.get("type", "soft").lower()  # hard / soft
        decision_on_hit = boundary.get("decision", "REVIEW").upper()

        for rule in boundary.get("rules", []):
            when = rule.get("when", {})
            if not isinstance(when, dict):
                continue

            if match_when(when, ctx):
                violations.append(
                    Violation(
                        boundary=key,
                        rule_id=str(rule.get("id", "unknown_rule")),
                        severity=str(rule.get("severity", "unknown")),
                        message=str(rule.get("message", "")),
                    )
                )

                if btype == "hard":
                    return EvaluationResult(
                        decision="DENY",
                        violations=violations,
                        required_approvals=[],
                    )

                # soft boundary hit => REVIEW by default (collect approvals)
                if decision_on_hit == "DENY":
                    # If someone configures a soft boundary as deny, honor it.
                    return EvaluationResult(
                        decision="DENY",
                        violations=violations,
                        required_approvals=[],
                    )

                approvals.append({"boundary": key, "required": True})

        # Note: lexicographic implies we don't need to "continue" differently;
        # hard stops already returned. soft continues to collect.

    if approvals:
        return EvaluationResult(decision="REVIEW", violations=violations, required_approvals=approvals)

    return EvaluationResult(decision="ALLOW", violations=[], required_approvals=[])


# -----------------------------
# CLI
# -----------------------------

def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="VCDesign Policy Evaluator (reference)")
    p.add_argument("--policy", required=True, help="Policy file path (JSON-compatible YAML recommended)")
    p.add_argument("--proposal", required=True, help="Proposal JSON file path")
    args = p.parse_args(argv)

    policy_path = Path(args.policy)
    proposal_path = Path(args.proposal)

    # Load inputs
    try:
        policy = load_json_like_yaml(policy_path)
    except Exception as e:
        print(str(e), file=sys.stderr)
        return 2

    try:
        proposal = load_json(proposal_path)
    except Exception as e:
        print(f"[ERROR] Failed to load proposal JSON: {proposal_path}\n{e}", file=sys.stderr)
        return 2

    # Evaluate
    result = evaluate(policy, proposal)

    out = {
        "decision": result.decision,
        "violations": [
            {
                "boundary": v.boundary,
                "rule_id": v.rule_id,
                "severity": v.severity,
                "message": v.message,
            }
            for v in result.violations
        ],
        "required_approvals": result.required_approvals,
    }

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
