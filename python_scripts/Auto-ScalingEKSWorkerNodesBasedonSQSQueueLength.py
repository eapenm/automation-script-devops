import boto3
from kubernetes import client, config

sqs = boto3.client('sqs')
autoscaling = boto3.client('autoscaling')

def scale_eks_nodes(queue_url, autoscaling_group_name):
    queue_attrs = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])
    message_count = int(queue_attrs['Attributes']['ApproximateNumberOfMessages'])

    if message_count > 50:
        autoscaling.set_desired_capacity(AutoScalingGroupName=autoscaling_group_name, DesiredCapacity=5)
    else:
        autoscaling.set_desired_capacity(AutoScalingGroupName=autoscaling_group_name, DesiredCapacity=1)

def lambda_handler(event, context):
    scale_eks_nodes('your-sqs-queue-url', 'your-eks-autoscaling-group')
