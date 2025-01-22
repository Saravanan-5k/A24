import boto3

client = boto3.client('s3',aws_access_key_id='AKIAWV2OKSGTMOICQ36H',aws_secret_access_key='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')

def create_bucket(bucket_name):
        try:
            bucket = client.create_bucket(
                Bucket=bucket_name,
            )
            print('{bucket} created successfully')
        except Exception as e:
            print('error : {e}')    


bucket_name = 'sun-day' 

create_bucket(bucket_name)

 
