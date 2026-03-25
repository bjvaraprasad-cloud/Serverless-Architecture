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