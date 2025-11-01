import json
import boto3
import os

# DynamoDB setup
dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ.get("TASK_TABLE_NAME", "TaskTable")
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    http_method = event.get("httpMethod", "")
    
    if http_method == "GET":
        return get_tasks()
    elif http_method == "POST":
        body = json.loads(event.get("body", "{}"))
        return create_task(body)
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({"message": f"Method {http_method} not allowed"})
        }

def get_tasks():
    response = table.scan()
    tasks = response.get("Items", [])
    return {
        "statusCode": 200,
        "body": json.dumps({"tasks": tasks})
    }

def create_task(body):
    task_id = body.get("id")
    description = body.get("description")
    
    if not task_id or not description:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Task must have 'id' and 'description'"})
        }

    table.put_item(Item={"id": task_id, "description": description})
    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Task created"})
    }
