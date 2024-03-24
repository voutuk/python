import boto3, random, paramiko, time, json
from secrets import access_key, secret_key


# Create a bucket policy
bucket_name = 'voutuks'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
region = 'eu-north-1'

s3 = boto3.client('s3', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

try:
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    print("Bucket policy successfully set!")
except Exception as e:
    print("An error occurred:", e)
