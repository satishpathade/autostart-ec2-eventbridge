# autostart-ec2-eventbridge

A serverless solution to automatically **start EC2 instances** on a schedule using **AWS Lambda** and **Amazon EventBridge**.

## Overview
This project helps you save costs by ensuring EC2 instances only run when needed.  
EventBridge triggers a Lambda function that starts your EC2 instance(s) at a specified time.

## Architecture
1. **Amazon EventBridge** – defines the schedule (cron/interval).
2. **AWS Lambda (Python)** – runs a script with `boto3` to start EC2 instances.
3. **Amazon EC2** – the target instance(s) you want to start.

## Setup⚡

1. **Create IAM Role for Lambda**  
   - Trust policy → allow `lambda.amazonaws.com`  
   - Permissions → `ec2:StartInstances` + CloudWatch Logs

2. **Create Lambda Function**  
   - Runtime: Python 3.9+  
   - Upload `autostartec2.py`  
   - Replace `instance_ids` with your EC2 ID(s)  

3. **Create EventBridge Rule**  
   - Add cron or rate expression (e.g., `cron(0 9 * * ? *)` = every day 9 AM)  
   - Set target = your Lambda function  

That’s it. Your EC2 will auto-start on schedule.
