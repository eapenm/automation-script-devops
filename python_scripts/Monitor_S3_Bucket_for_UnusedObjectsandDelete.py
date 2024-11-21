import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')

def delete_old_objects(bucket_name, days):
    threshold_date = datetime.now() - timedelta(days=days)
    objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']
    
    for obj in objects:
        last_modified = obj['LastModified']
        if last_modified < threshold_date:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

bucket_name = 'your-bucket-name'
delete_old_objects(bucket_name, 30)
