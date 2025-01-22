import boto3

client = boto3.client('s3',aws_access_key_id=,aws_secret_access_key=)

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

 
