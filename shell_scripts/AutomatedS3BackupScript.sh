#!/bin/bash

BUCKET_NAME="your-bucket-name"
BACKUP_DIR="/path/to/backup"

aws s3 sync $BACKUP_DIR s3://$BUCKET_NAME/backup --delete
