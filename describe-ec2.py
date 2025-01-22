import boto3

client = boto3.client('ec2',aws_access_key_id=,aws_secret_access_key=)
def exit_instance(instance_id):
    response = client.describe_instances(InstanceIds=[instance_id])
    instance=response['Reservations'][0]['Instances'][0]
    
    print(instance)
        
instance_id="i-00ced5ec3dbd7ce28"    
exit_instance(instance_id)