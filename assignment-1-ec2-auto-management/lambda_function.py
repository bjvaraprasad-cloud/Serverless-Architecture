import boto3

def lambda_handler(event, context):
    print("Lambda execution started")

    ec2 = boto3.client('ec2')

    # STOP instances
    stop_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
            {'Name': 'instance-state-name', 'Values': ['running']}
        ]
    )

    stop_ids = []
    for res in stop_response['Reservations']:
        for inst in res['Instances']:
            stop_ids.append(inst['InstanceId'])

    print("Stop IDs found:", stop_ids)

    if stop_ids:
        ec2.stop_instances(InstanceIds=stop_ids)
        print("Stopped instances:", stop_ids)

    # START instances
    start_response = ec2.describe_instances(
        Filters=[
            {'Name': 'tag:Action', 'Values': ['Auto-Start']},
            {'Name': 'instance-state-name', 'Values': ['stopped']}
        ]
    )

    start_ids = []
    for res in start_response['Reservations']:
        for inst in res['Instances']:
            start_ids.append(inst['InstanceId'])

    print("Start IDs found:", start_ids)

    if start_ids:
        ec2.start_instances(InstanceIds=start_ids)
        print("Started instances:", start_ids)

    return "Done"
