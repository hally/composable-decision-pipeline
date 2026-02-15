from .beads.normalize import normalize
from .beads.threshold_check import threshold_check
from .beads.policy_check import policy_check
from .beads.decision import decide
from .beads.explain import explain

def run_pipeline(payload: dict) -> dict:
    trace = []

    ctx = normalize(payload, trace)
    ctx = threshold_check(ctx, trace)
    ctx = policy_check(ctx, trace)
    ctx = decide(ctx, trace)
    result = explain(ctx, trace)

    return result
