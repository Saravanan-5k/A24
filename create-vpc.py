import boto3

client = boto3.client('ec2',aws_access_key_id='AKIAWV2OKSGTMOICQ36H',aws_secret_access_key='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')
vpc_create = client.create_vpc(
    CidrBlock='10.1.0.0/16',
  
)
vpc_id = vpc_create['Vpc']['VpcId']
print(vpc_id)
subnet_create = client.create_subnet(
    
    CidrBlock='10.1.1.0/24',
    VpcId=vpc_id,
    
)
subnet_id = subnet_create['Subnet']['SubnetId']
print(subnet_id)