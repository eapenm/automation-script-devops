import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def manage_ec2_instances(instance_ids, action):
    if action == 'start':
        ec2.start_instances(InstanceIds=instance_ids)
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instance_ids)

def lambda_handler(event, context):
    current_hour = datetime.now().hour
    instance_ids = ['i-xxxxxx', 'i-yyyyyy']
    
    if 9 <= current_hour < 18:
        manage_ec2_instances(instance_ids, 'start')
    else:
        manage_ec2_instances(instance_ids, 'stop')
