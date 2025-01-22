import boto3

client = boto3.client('s3',aws_access_key_id=,aws_secret_access_key=)

response = client.list_buckets()
#print(response['Buckets'])
for i in response['Buckets']:
    print(i['Name'],i['CreationDate'])
   