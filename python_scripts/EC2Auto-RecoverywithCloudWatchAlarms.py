import boto3

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def check_alarm_status(instance_id):
    alarms = cloudwatch.describe_alarms(StateValue='ALARM')['MetricAlarms']
    for alarm in alarms:
        if 'CPUUtilization' in alarm['MetricName'] and alarm['StateValue'] == 'ALARM':
            ec2.reboot_instances(InstanceIds=[instance_id])

def lambda_handler(event, context):
    check_alarm_status('your-instance-id')
