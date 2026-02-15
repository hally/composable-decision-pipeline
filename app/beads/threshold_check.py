def threshold_check(ctx: dict, trace: list) -> dict:
    threshold = ctx["policy"]["threshold_pct"]
    actual = ctx["cost_delta_pct"]

    triggered = actual >= threshold
    ctx["flags"]["threshold_breach"] = triggered

    if triggered:
        ctx["reason_codes"].append("THRESHOLD_BREACH")

    trace.append({
        "bead": "threshold_check",
        "outcome": "triggered" if triggered else "not_triggered",
        "details": {"threshold_pct": threshold, "actual_pct": actual}
    })
    return ctx
