import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        name = bucket['Name']

        try:
            response = s3.get_bucket_encryption(Bucket=name)
            enc = response['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            
            print(f"Bucket: {name}  Encryption Type: {enc}")

        except Exception:
            print(f"Bucket: {name}  No Encryption Found")