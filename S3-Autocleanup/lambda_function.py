import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')
BUCKET_NAME = 'vara-s3-cleanup'

def lambda_handler(event, context):
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    for obj in response['Contents']:
        file_age = datetime.now(timezone.utc) - obj['LastModified']

        if file_age > timedelta(minutes=1):   #  changed here
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
            print(f"Deleted: {obj['Key']}")
        else:
            print(f"Kept: {obj['Key']}")