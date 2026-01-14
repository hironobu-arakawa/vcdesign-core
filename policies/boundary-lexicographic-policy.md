version: 1
policy_id: boundary_lexico_v1
name: Boundary Lexicographic Order
description: >
  Lexicographic boundary order for Always-on Rapid Optimization.
  Higher-priority boundaries must never be violated for lower-level gains.

# 辞書式優先順位（上ほど絶対）
lexicographic_order:
  - SAFETY
  - COMPLIANCE
  - TRUST
  - ETHICS
  - BUSINESS_VIABILITY
  - KPI_EFFICIENCY

boundaries:
  SAFETY:
    type: hard
    principle: "Never increase risk to human life, body, or catastrophic equipment事故."
    decision: "DENY"
    rules:
      - id: safety.no_margin_reduction
        severity: critical
        when:
          any:
            - field: proposal.effects.safety_margin_delta
              op: "<"
              value: 0
            - field: proposal.effects.incident_risk_delta
              op: ">"
              value: 0
        message: "Safety margin reduced or incident risk increased."

  COMPLIANCE:
    type: hard
    principle: "Never violate laws, regulations, or mandatory procedures."
    decision: "DENY"
    rules:
      - id: compliance.violation_detected
        severity: critical
        when:
          any:
            - field: proposal.flags.compliance_violation
              op: "=="
              value: true
        message: "Compliance violation detected."

  TRUST:
    type: hard
    principle: "Never optimize toward long-term trust erosion."
    decision: "DENY"
    rules:
      - id: trust.data_integrity_down
        severity: high
        when:
          any:
            - field: proposal.effects.data_integrity_delta
              op: "<"
              value: 0
            - field: proposal.effects.auditability_delta
              op: "<"
              value: 0
        message: "Trust boundary: data integrity or auditability degraded."

  ETHICS:
    type: hard
    principle: "Never optimize toward unfairness, hidden surveillance, or concealment."
    decision: "DENY"
    rules:
      - id: ethics.unfairness_up
        severity: high
        when:
          any:
            - field: proposal.effects.fairness_delta
              op: "<"
              value: 0
            - field: proposal.flags.hidden_monitoring
              op: "=="
              value: true
        message: "Ethics boundary: fairness decreased or hidden monitoring enabled."

  BUSINESS_VIABILITY:
    type: soft
    principle: "Business viability is important but redesignable; allow only with explicit approval."
    decision: "REVIEW"
    rules:
      - id: biz.viability_down
        severity: medium
        when:
          any:
            - field: proposal.effects.business_viability_delta
              op: "<"
              value: 0
        message: "Business viability decreased; requires review/approval."

  KPI_EFFICIENCY:
    type: soft
    principle: "KPI improvements are allowed if higher boundaries are preserved."
    decision: "ALLOW"
    rules:
      - id: kpi.improve
        severity: info
        when:
          all:
            - field: proposal.effects.kpi_delta
              op: ">"
              value: 0
        message: "KPI improved (soft objective)."

# 境界衝突時の扱い（Lexicographic）
conflict_resolution:
  mode: lexicographic
  hard_violation_action: DENY
  soft_violation_action: REVIEW
  require_explanations: true

# 出力（監査用）
audit:
  log_level: "decision"
  record_fields:
    - proposal.id
    - proposal.title
    - proposal.actor
    - proposal.effects
    - evaluation.decision
    - evaluation.violations
    - evaluation.required_approvals
