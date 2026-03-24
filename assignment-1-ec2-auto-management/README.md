# Assignment 1: EC2 Automated Instance Management

## Objective
Automate start and stop of EC2 instances using AWS Lambda and Boto3 based on tags.

## Services Used
- AWS Lambda
- Amazon EC2
- IAM
- CloudWatch
- Boto3 (Python SDK)
Created new EC2 instances as part of this task status as running.PFA
<img width="803" height="113" alt="image" src="https://github.com/user-attachments/assets/c1944374-c1f6-4af6-8054-04cf1c93dec3" />



## Tags Configuration
- Action = Auto-Stop → Stops instance
- Action = Auto-Start → Starts instance
- <img width="514" height="179" alt="image" src="https://github.com/user-attachments/assets/64bd5667-c088-4783-bc8e-1e3e4f3e530a" />

<img width="521" height="243" alt="image" src="https://github.com/user-attachments/assets/b0090ed1-8ca6-4a89-9dbc-0459310e582c" />



## Workflow
1. Lambda function triggered manually
2. Boto3 checks EC2 instances
3. Filters instances based on tags
4. Stops or starts instances accordingly
5. Logs stored in CloudWatch

<img width="533" height="259" alt="image" src="https://github.com/user-attachments/assets/1d5c208c-ca90-4aed-8be4-42fc78c877b6" />




## Result
- Successfully automated EC2 instance management
- Instances changed state based on tags
-
- <img width="830" height="156" alt="image" src="https://github.com/user-attachments/assets/a3b735df-5773-43e2-95b3-5a010795f34c" />

<img width="544" height="314" alt="image" src="https://github.com/user-attachments/assets/85dcab5a-8317-4d98-8f3c-56b4a6721055" />


Debug erroe missing one more policy found this error while test the code added new policy and provide correct tag names:-
<img width="547" height="197" alt="image" src="https://github.com/user-attachments/assets/0e58cf29-c90d-4c12-a7f0-93e60cec59f5" />



## Security
- IAM role with least required permissions
- SSH access restricted to My IP

## Instance Details
- OS: Amazon Linux
- Type: t2.micro
