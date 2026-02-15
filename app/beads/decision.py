def decide(ctx: dict, trace: list) -> dict:
    breach = ctx["flags"].get("threshold_breach", False)
    policy = ctx["flags"].get("policy_requires_escalation", False)

    # Decision rule: escalate if threshold breach OR critical policy triggers
    decision = "ESCALATE" if (breach or policy) else "IGNORE"
    ctx["decision"] = decision

    trace.append({
        "bead": "decision",
        "outcome": decision,
        "details": {"threshold_breach": breach, "policy_requires_escalation": policy}
    })
    return ctx
