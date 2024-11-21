import boto3

ec2 = boto3.client('ec2')

def check_compliance(security_group):
    for permission in security_group['IpPermissions']:
        if permission['IpProtocol'] == '-1':  # Catch all protocols
            return False  # Violates policy
    return True

def remediate_non_compliance(group_id):
    ec2.revoke_security_group_ingress(GroupId=group_id, IpPermissions=[{'IpProtocol': '-1'}])

def lambda_handler(event, context):
    security_groups = ec2.describe_security_groups()['SecurityGroups']
    for sg in security_groups:
        if not check_compliance(sg):
            remediate_non_compliance(sg['GroupId'])
