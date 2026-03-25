Assignment 5: Auto Tag EC2 on Launch
 Objective

 # Assignment 5: Auto-Tagging EC2 Instances on Launch

## Objective
Automatically tag any newly launched EC2 instance in AWS with the current date and a custom owner tag. This ensures better tracking, management, and accountability of cloud resources.

## Overview
This solution uses **AWS Lambda** and **EventBridge (CloudWatch Events)**:

1. **EventBridge Rule**  
   - Monitors EC2 instance state changes.  
   - Triggers the Lambda function when an instance enters the `running` state.

2. **Lambda Function**  
   - Written in Python using **Boto3**.  
   - Receives the instance ID from the EventBridge event.  
   - Tags the instance with:
     - `Owner` → Custom name (e.g., "Vara")
     - `LaunchedOn` → Current date (YYYY-MM-DD)  
   - Provides log output for confirmation.

## Lambda Code (Python)


>Whenever a new EC2 instance is created,It should automatically get a tag

EC2 Launch>>Event Trigger>>Lambda>>Add Tag

Created Role with two polices attached as per part if this task to assign auto tags.

<img width="772" height="342" alt="image" src="https://github.com/user-attachments/assets/c2186897-cd09-42fb-a62a-cbf7a2a2fbd8" />

Created Lambda fucntion with Role name attached as LambdaAutoTagEC2Role by using python 3.14 version

<img width="464" height="193" alt="image" src="https://github.com/user-attachments/assets/6a9bbd83-c991-4bb0-a5ea-b1fc48c1d14e" />

Added lambda code and deployed succesfully.

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    # Get instance ID from event
    instance_id = event['detail']['instance-id'] 
    print("New Instance ID:", instance_id)
    # Add tag
    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                'Key': 'Owner',
                'Value': 'Vara'
            }
        ]
    )
    print("Tag added successfully")
    return "Done"

Getting error while testing the lambda functions so i changed lambda function withlatest code.
<img width="662" height="325" alt="image" src="https://github.com/user-attachments/assets/27ae80bf-fff8-46c5-87a8-5bcdef77417d" />

 <img width="513" height="127" alt="image" src="https://github.com/user-attachments/assets/5b93ef7f-9c9c-41e5-a0b2-bb382182bf3c" />


   After testing resuts are added.

