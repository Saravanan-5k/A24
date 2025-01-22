import boto3

def Iam_Users(a):
   client = boto3.client('iam',aws_access_key_id=,aws_secret_access_key=)
   response = client.list_users()
   #print(response)
   for i in response['Users']:
    print(i['Arn'],i['UserName'])
def main():
    print('Userss')
    a='User Lists'
    Iam_Users(a)
main()    