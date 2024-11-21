import boto3

ec2 = boto3.client('ec2')

def create_snapshot(volume_id):
    ec2.create_snapshot(VolumeId=volume_id, Description='Automated backup snapshot')

def lambda_handler(event, context):
    volumes = ec2.describe_volumes()['Volumes']
    for volume in volumes:
        create_snapshot(volume['VolumeId'])
