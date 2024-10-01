<h1 align="center">💻AWS-Simple-Log-Service💻</h1>

## 🌟 Basic Overview
A serverless logging service built using AWS Lambda, designed to capture and log messages with varying levels of severity.

![HTTP api](https://github.com/user-attachments/assets/4ccf765d-eeb3-46cf-9b59-7cb2e72fffcc)

## Description
The AWS-Simple-Log-Service allows clients to post and retrieve log entries via an HTTP API. It handles both POST and GET requests, storing logs in AWS CloudWatch for real-time monitoring. AWS Lambda executes the logic for processing and retrieving logs, while API Gateway manages the HTTP requests. This serverless setup offers an efficient and scalable solution for cloud-based log management.

## 🔅 Key Features
- Log Entry Creation: Processes incoming events and dynamically logs entries based on severity levels ("info," "warning," or "error"). It validates the input data and ensures proper formatting.

![SaveLogEntry](https://github.com/user-attachments/assets/bfae0010-7a86-40bf-9a56-09f30a25ca59)

- Log Retrieval: This essential function retrieves the last 100 log entries from AWS CloudWatch Logs, allowing users to access and review recent log data quickly.

![RetreiveLogEntry](https://github.com/user-attachments/assets/064e2002-8da6-4b09-9896-970e7361a971)

- Dynamic Severity Levels: Supports logging for different severity levels (info, warning, error).
- Error Handling: Validates incoming data to ensure correct formatting and provides appropriate error messages.
- Serverless Architecture: Built using AWS Lambda for scalability and cost-efficiency.

## 📥 Installation 
-  1.	Clone this repository
-  2. Set up your AWS Lambda function: [Visit AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
-  3.
