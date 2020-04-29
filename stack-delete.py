import boto3
import json
from botocore.exceptions import ClientError

def delete_cfn(stack_name):
    try:
        cfn = boto3.resource('cloudformation')
        stack = cfn.Stack(stack_name)
        stack.delete()
        return "SUCCESS"
    except ClientError as e:
        print(f"Error: {e}")
        return "ERROR" 

def handler(event, context):
    print("Received event:")
    print(json.dumps(event))
    stack_name = event['stack_name']
    status = delete_cfn(stack_name)
    print(status)
    return status