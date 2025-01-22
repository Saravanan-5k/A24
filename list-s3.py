import boto3

client = boto3.client('s3',aws_access_key_id='AKIAWV2OKSGTMOICQ36H',aws_secret_access_key='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')

response = client.list_buckets()
#print(response['Buckets'])
for i in response['Buckets']:
    print(i['Name'],i['CreationDate'])
   