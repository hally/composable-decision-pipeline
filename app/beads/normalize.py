def normalize(payload: dict, trace: list) -> dict:
    """
    Normalize/validate input into a context dict.
    """
    # defaults
    policy = payload.get("policy") or {}
    ctx = {
        "cost_delta_pct": float(payload.get("cost_delta_pct", 0)),
        "service_tier": str(payload.get("service_tier", "standard")).lower(),
        "vendor": str(payload.get("vendor", "unknown")).lower(),
        "policy": {
            "threshold_pct": float(policy.get("threshold_pct", 20)),
            "escalate_on_critical": bool(policy.get("escalate_on_critical", True)),
        },
        "flags": {},
        "decision": None,
        "reason_codes": [],
    }

    trace.append({
        "bead": "normalize",
        "outcome": "ok",
        "details": {
            "service_tier": ctx["service_tier"],
            "cost_delta_pct": ctx["cost_delta_pct"],
            "threshold_pct": ctx["policy"]["threshold_pct"],
        }
    })
    return ctx
