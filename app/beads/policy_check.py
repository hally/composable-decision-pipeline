def policy_check(ctx: dict, trace: list) -> dict:
    tier = ctx["service_tier"]
    escalate_on_critical = ctx["policy"]["escalate_on_critical"]

    critical = tier == "critical"
    ctx["flags"]["critical_service"] = critical

    triggered = critical and escalate_on_critical
    ctx["flags"]["policy_requires_escalation"] = triggered

    if triggered:
        ctx["reason_codes"].append("CRITICAL_SERVICE")

    trace.append({
        "bead": "policy_check",
        "outcome": "triggered" if triggered else "not_triggered",
        "details": {"service_tier": tier, "escalate_on_critical": escalate_on_critical}
    })
    return ctx
