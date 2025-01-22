import boto3

def Iam_Users(a):
   client = boto3.client('iam',aws_access_key_id='AKIAWV2OKSGTMOICQ36H',aws_secret_access_key='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')
   response = client.list_users()
   #print(response)
   for i in response['Users']:
    print(i['Arn'],i['UserName'])
def main():
    print('Userss')
    a='User Lists'
    Iam_Users(a)
main()    