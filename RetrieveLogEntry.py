import boto3
import json
from datetime import datetime, timedelta
import time

def lambda_handler(event, context):
    client = boto3.client('logs')
    
    # Calculate the time range for the past hour
    end_time = datetime.now()  # Current time
    start_time = end_time - timedelta(hours=1)  # 1 hour ago
    
    # Convert times to Unix timestamps (milliseconds)
    start_timestamp = int(start_time.timestamp() * 1000)
    end_timestamp = int(end_time.timestamp() * 1000)
    
    # Specify the log group name
    log_group_name = '/aws/lambda/SaveLogEntry'
    
    # Start a query to get the last 100 log entries from the past hour,
    # filtering for logs that contain "ID: " in their message.
    response = client.start_query(
        logGroupName=log_group_name,
        startTime=start_timestamp,
        endTime=end_timestamp,
        queryString='fields @timestamp, @message | filter @message like /ID: / | sort @timestamp desc | limit 100'
    )
    
    query_id = response['queryId']
    
    # Wait for the query to complete
    while True:
        response = client.get_query_results(queryId=query_id)
        if response['status'] == 'Complete':
            break
        time.sleep(1)
    
    # Extract the log results
    log_results = response['results']
    
    # Prepare a list to store formatted log entries
    formatted_results = []
    
    # Process each log result
    for log in log_results:
        # The log message is contained in the @message field
        log_message = next((field['value'] for field in log if field['field'] == '@message'), '')
        
        # Split the log message into components
        log_parts = log_message.split('\n')
        log_dict = {}
        
        # Parse each part into a dictionary
        for part in log_parts:
            if ': ' in part:
                key, value = part.split(': ', 1)
                log_dict[key.strip()] = value.strip()
        
        # Format the log entry for output
        formatted_entry = (
            f"ID: {log_dict.get('ID', 'N/A')}\n"
            f"DateTime: {log_dict.get('DateTime', 'N/A')}\n"
            f"Severity: {log_dict.get('Severity', 'N/A')}\n"
            f"Message: {log_dict.get('Message', 'N/A')}\n"
        )
        formatted_results.append(formatted_entry)
    
    # Check if no logs were found
    if not formatted_results:
        return {
            'statusCode': 200,
            'body': 'No log entries found.'  # Return a message if no logs are available
        }
    
    # Return the logs instead of a success message
    return {
        'statusCode': 200,
        'body': '\n'.join(formatted_results)  # Return the formatted logs as a single string
    }
