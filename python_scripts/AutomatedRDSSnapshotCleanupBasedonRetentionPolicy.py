import boto3
from datetime import datetime, timedelta

rds = boto3.client('rds')

def delete_old_snapshots(retention_days):
    retention_date = datetime.now() - timedelta(days=retention_days)
    snapshots = rds.describe_db_snapshots()['DBSnapshots']
    
    for snapshot in snapshots:
        if snapshot['SnapshotCreateTime'] < retention_date:
            rds.delete_db_snapshot(DBSnapshotIdentifier=snapshot['DBSnapshotIdentifier'])

delete_old_snapshots(7)
