def explain(ctx: dict, trace: list) -> dict:
    # Create a clean response shape
    result = {
        "decision": ctx["decision"],
        "reason_codes": ctx["reason_codes"],
        "trace": trace
    }
    trace.append({"bead": "explain", "outcome": "ok"})
    return result
