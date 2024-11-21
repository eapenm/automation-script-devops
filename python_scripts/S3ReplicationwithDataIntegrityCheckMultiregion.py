import boto3
import hashlib

s3 = boto3.client('s3')

def calculate_checksum(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def replicate_objects(source_bucket, destination_bucket, object_key):
    source_object = s3.get_object(Bucket=source_bucket, Key=object_key)
    s3.put_object(Bucket=destination_bucket, Key=object_key, Body=source_object['Body'].read())
    
    source_checksum = calculate_checksum(source_object['Body'].read())
    dest_object = s3.get_object(Bucket=destination_bucket, Key=object_key)
    dest_checksum = calculate_checksum(dest_object['Body'].read())
    
    if source_checksum == dest_checksum:
        print(f'{object_key} successfully replicated with matching checksum.')

def lambda_handler(event, context):
    replicate_objects('source-bucket-name', 'destination-bucket-name', 'your-object-key')
