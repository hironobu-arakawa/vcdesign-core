package vcdesign.boundary

default decision := "ALLOW"
default violations := []
default required_approvals := []

# --- Hard boundaries (DENY) ---

deny[msg] {
  input.proposal.effects.safety_margin_delta < 0
  msg := {"boundary":"SAFETY", "rule":"safety.no_margin_reduction", "severity":"critical",
          "message":"Safety margin reduced."}
}

deny[msg] {
  input.proposal.effects.incident_risk_delta > 0
  msg := {"boundary":"SAFETY", "rule":"safety.risk_increase", "severity":"critical",
          "message":"Incident risk increased."}
}

deny[msg] {
  input.proposal.flags.compliance_violation == true
  msg := {"boundary":"COMPLIANCE", "rule":"compliance.violation_detected", "severity":"critical",
          "message":"Compliance violation detected."}
}

deny[msg] {
  input.proposal.effects.data_integrity_delta < 0
  msg := {"boundary":"TRUST", "rule":"trust.data_integrity_down", "severity":"high",
          "message":"Data integrity degraded."}
}

deny[msg] {
  input.proposal.effects.auditability_delta < 0
  msg := {"boundary":"TRUST", "rule":"trust.auditability_down", "severity":"high",
          "message":"Auditability degraded."}
}

deny[msg] {
  input.proposal.flags.hidden_monitoring == true
  msg := {"boundary":"ETHICS", "rule":"ethics.hidden_monitoring", "severity":"high",
          "message":"Hidden monitoring enabled."}
}

deny[msg] {
  input.proposal.effects.fairness_delta < 0
  msg := {"boundary":"ETHICS", "rule":"ethics.unfairness_up", "severity":"high",
          "message":"Fairness decreased."}
}

# --- Soft boundaries (REVIEW) ---

review[msg] {
  input.proposal.effects.business_viability_delta < 0
  msg := {"boundary":"BUSINESS_VIABILITY", "rule":"biz.viability_down", "severity":"medium",
          "message":"Business viability decreased; requires approval."}
}

# --- Final decision composition ---

decision := "DENY" {
  some msg
  deny[msg]
}

decision := "REVIEW" {
  not decision == "DENY"
  some msg
  review[msg]
}

violations[msg] {
  deny[msg]
}

violations[msg] {
  review[msg]
}

required_approvals[app] {
  review[_]
  app := {"boundary":"BUSINESS_VIABILITY", "required": true}
}
