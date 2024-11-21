import boto3

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')

def scale_ec2():
    alarms = cloudwatch.describe_alarms()['MetricAlarms']
    for alarm in alarms:
        if alarm['StateValue'] == 'ALARM' and alarm['MetricName'] == 'CPUUtilization':
            # Example action: Launch a new instance
            ec2.run_instances(
                ImageId='ami-xxxxxx',
                InstanceType='t2.micro',
                MinCount=1, MaxCount=1
            )

def lambda_handler(event, context):
    scale_ec2()
