import json
import os
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = os.environ['TABLE_NAME']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    path_params = event.get("pathParameters") or {}
    body = event.get("body")
    if body:
        body = json.loads(body)

    if http_method == "GET":
        task_id = path_params.get("id")
        if task_id:
            return get_task(task_id)
        else:
            return list_tasks()
    elif http_method == "POST":
        return create_task(body)
    elif http_method == "PUT":
        task_id = path_params.get("id")
        return update_task(task_id, body)
    elif http_method == "DELETE":
        task_id = path_params.get("id")
        return delete_task(task_id)
    else:
        return respond(400, {"message": "Unsupported method"})

# ----- CRUD Operations -----
def list_tasks():
    response = table.scan()
    return respond(200, {"tasks": response.get("Items", [])})

def get_task(task_id):
    response = table.get_item(Key={"id": task_id})
    item = response.get("Item")
    if not item:
        return respond(404, {"message": "Task not found"})
    return respond(200, item)

def create_task(task):
    if "id" not in task:
        return respond(400, {"message": "Task must have an 'id'"})
    table.put_item(Item=task)
    return respond(201, task)

def update_task(task_id, updates):
    response = table.get_item(Key={"id": task_id})
    item = response.get("Item")
    if not item:
        return respond(404, {"message": "Task not found"})
    item.update(updates)
    table.put_item(Item=item)
    return respond(200, item)

def delete_task(task_id):
    response = table.get_item(Key={"id": task_id})
    if "Item" not in response:
        return respond(404, {"message": "Task not found"})
    table.delete_item(Key={"id": task_id})
    return respond(200, {"message": f"Task {task_id} deleted"})

# ----- Helper -----
def respond(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
