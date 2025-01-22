import boto3

def list_unattached_volumes():
    
    ec2 = boto3.client('ec2',aws_access_key_id=,aws_secret_access_key=)
    

    response = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    volumes = response.get('Volumes', [])
    

    volume_details = []
    for volume in volumes:
        volume_details.append(f"Volume ID: {volume['VolumeId']}, Size: {volume['Size']} GiB, Availability Zone: {volume['AvailabilityZone']}")
    
    return "\n".join(volume_details)

def send_email(volume_details):
    
    ses = boto3.client('ses', region_name='us-east-1')  
    
    
    sender = "msaravnan29398@gmail.com"
    recipient = "saravanan980329@gmil.com"
    subject = "Unattached EBS Volumes Report"
    body = f"The following EBS volumes are unattached:\n\n{volume_details}" if volume_details else "No unattached volumes found."
    
    
    response = ses.send_email(
        Source=sender,
        Destination={
            'ToAddresses': [recipient],
        },
        Message={
            'Subject': {
                'Data': subject,
            },
            'Body': {
                'Text': {
                    'Data': body,
                }
            }
        }
    )
    print("Email sent! Message ID:", response['MessageId'])


if __name__ == "__main__":
    unattached_volumes = list_unattached_volumes()
    send_email(unattached_volumes)
