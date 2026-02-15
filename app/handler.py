import json
from .pipeline import run_pipeline

def lambda_handler(event, context):
    # HTTP API (payload v2.0) puts body in event["body"]
    body_raw = event.get("body") or "{}"
    try:
        payload = json.loads(body_raw) if isinstance(body_raw, str) else body_raw
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {"content-type": "application/json"},
            "body": json.dumps({"error": "Invalid JSON body"})
        }

    result = run_pipeline(payload)

    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(result),
    }
