import json
from datetime import datetime
import platform

def lambda_handler(event, context):
    message = {
        "title": "ElevateLab Lambda Function",
        "message": "Your serverless function is live and running smoothly!",
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "runtime": platform.python_version(),
        "status": "Success"
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(message, indent=2)
    }
