import boto3
import datetime
import json
import uuid

def lambda_handler(event, context):
    # Extract the body from the event
    body = json.loads(event['body'])
    
    # Generate a unique ID for the log entry
    log_id = str(uuid.uuid4())
    
    # Get the current UTC time
    log_datetime = datetime.datetime.utcnow().isoformat()
    
    # Extract log entry details from the body
    log_severity = body['Severity']
    log_message = body['Message']
    
    
    # Create the log entry content
    log_entry = f"ID: {log_id}\nDateTime: {log_datetime}\nSeverity: {log_severity}\nMessage: {log_message}"
    
    # Save the log entry to CloudWatch Logs
    log_group_name = f"/aws/lambda/{context.function_name}"
    log_stream_name = context.log_stream_name
    
    logs = boto3.client('logs')
    response = logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': int(datetime.datetime.now().timestamp() * 1000),
                'message': log_entry
            }
        ],
        sequenceToken=context.aws_request_id
    )
    
    return {
        'statusCode': 200,
        'body': 'Log entry saved successfully'
    }
