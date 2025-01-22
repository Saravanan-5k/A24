import boto3

client = boto3.client('iam',aws_access_key_id='AKIAWV2OKSGTMOICQ36H',aws_secret_access_key='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')
def create_user( ):
 try:   
  response = client.create_user(
    UserName='Hulk',
 )
  iam_user=response['User']['UserName']
  print("user{iam_user} created sucessfully")

 except Exception as e :
    print('an error occured : {e}')
create_user()