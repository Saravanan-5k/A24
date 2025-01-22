import boto3

client = boto3.client('iam',aws_access_key_id=,aws_secret_access_key=)

response = client.list_users()
