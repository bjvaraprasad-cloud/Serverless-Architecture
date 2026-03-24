# Assignment 1: EC2 Automated Instance Management

## Objective
Automate start and stop of EC2 instances using AWS Lambda and Boto3 based on tags.

## Services Used
- AWS Lambda
- Amazon EC2
- IAM
- CloudWatch
- Boto3 (Python SDK)

## Tags Configuration
- Action = Auto-Stop → Stops instance
- Action = Auto-Start → Starts instance

## Workflow
1. Lambda function triggered manually
2. Boto3 checks EC2 instances
3. Filters instances based on tags
4. Stops or starts instances accordingly
5. Logs stored in CloudWatch

## Result
- Successfully automated EC2 instance management
- Instances changed state based on tags

## Security
- IAM role with least required permissions
- SSH access restricted to My IP

## Instance Details
- OS: Amazon Linux
- Type: t2.micro
