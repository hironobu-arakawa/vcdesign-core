#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
run_all.py

Run policy evaluation for all example proposals and print a summary.

- Finds: examples/proposal*.json (default)
- Evaluates each proposal against the given policy
- Prints: decision + violations (count) + approvals (count)
- Optional: expected outcomes via --expect-map (JSON mapping file)

Exit codes:
- 0: all ok
- 2: input/load error
- 3: expectation mismatch (when --expect-map is used)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Import evaluator from same directory
# (Keep run_all.py in tools/policy-evaluator/)
from evaluator import evaluate, load_json_like_yaml, load_json  # type: ignore


def find_proposals(examples_dir: Path, pattern: str) -> List[Path]:
    return sorted(examples_dir.glob(pattern))


def short(s: str, n: int = 80) -> str:
    s = s.replace("\n", " ").strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def load_expect_map(path: Path) -> Dict[str, str]:
    """
    Expect map format (JSON):
      {
        "proposal_allow_kpi.json": "ALLOW",
        "proposal_review_business.json": "REVIEW",
        "proposal_deny_safety.json": "DENY"
      }
    Keys can also be proposal.id (we support both).
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("expect-map must be a JSON object (dict).")
    # normalize to uppercase strings
    out: Dict[str, str] = {}
    for k, v in data.items():
        out[str(k)] = str(v).upper()
    return out


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Run policy evaluation for all example proposals")
    p.add_argument(
        "--policy",
        default="policies/boundary-lexicographic-policy.json",
        help="Policy file path (JSON-compatible YAML/JSON). Default: policies/boundary-lexicographic-policy.json",
    )
    p.add_argument(
        "--examples-dir",
        default="examples",
        help="Examples directory. Default: examples",
    )
    p.add_argument(
        "--pattern",
        default="proposal*.json",
        help="Glob pattern under examples-dir. Default: proposal*.json",
    )
    p.add_argument(
        "--expect-map",
        default=None,
        help="Optional JSON file mapping (filename or proposal.id) -> expected decision",
    )
    args = p.parse_args(argv)

    repo_root = Path.cwd()
    policy_path = repo_root / args.policy
    examples_dir = repo_root / args.examples_dir

    # Load policy
    try:
        policy = load_json_like_yaml(policy_path)
    except Exception as e:
        print(f"[ERROR] Failed to load policy: {policy_path}\n{e}", file=sys.stderr)
        return 2

    # Find proposals
    proposals = find_proposals(examples_dir, args.pattern)
    if not proposals:
        print(f"[WARN] No proposal files found: {examples_dir}/{args.pattern}")
        return 0

    # Optional expectations
    expect: Optional[Dict[str, str]] = None
    if args.expect_map:
        try:
            expect = load_expect_map(repo_root / args.expect_map)
        except Exception as e:
            print(f"[ERROR] Failed to load expect-map: {args.expect_map}\n{e}", file=sys.stderr)
            return 2

    # Run all
    mismatches: List[Tuple[str, str, str]] = []  # (key, expected, actual)

    print("=== VCDesign policy-evaluator: run_all ===")
    print(f"Policy : {policy_path}")
    print(f"Target : {examples_dir}/{args.pattern}")
    if expect is not None:
        print(f"Expect : {repo_root / args.expect_map}")
    print("")

    header = f"{'file':40}  {'id':18}  {'decision':7}  {'viol#':5}  {'appr#':5}  title"
    print(header)
    print("-" * len(header))

    for path in proposals:
        try:
            proposal = load_json(path)
        except Exception as e:
            print(f"[ERROR] Failed to load proposal JSON: {path}\n{e}", file=sys.stderr)
            return 2

        result = evaluate(policy, proposal)

        proposal_id = str(proposal.get("id", ""))
        title = str(proposal.get("title", ""))

        viol_n = len(result.violations)
        appr_n = len(result.required_approvals)

        print(
            f"{path.name:40}  {proposal_id[:18]:18}  {result.decision:7}  {viol_n:5d}  {appr_n:5d}  {short(title)}"
        )

        # expectation check (if provided)
        if expect is not None:
            # key preference: filename -> proposal.id
            expected = None
            if path.name in expect:
                expected = expect[path.name]
                key = path.name
            elif proposal_id in expect:
                expected = expect[proposal_id]
                key = proposal_id
            else:
                expected = None

            if expected is not None:
                actual = result.decision.upper()
                if actual != expected:
                    mismatches.append((key, expected, actual))

    # Print details for mismatches / summary
    print("")
    if expect is not None:
        if mismatches:
            print("[FAIL] Expectation mismatches:")
            for key, exp, act in mismatches:
                print(f"  - {key}: expected={exp}, actual={act}")
            return 3
        print("[OK] All expectations matched.")

    print("[DONE]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
