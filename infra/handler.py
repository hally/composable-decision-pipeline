import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": json.dumps({
            "status": "ok",
            "message": "Composable Decision Pipeline is alive."
        }),
    }
