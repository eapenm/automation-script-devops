#!/bin/bash

LOG_GROUP_NAME="your-log-group"
S3_BUCKET="your-s3-bucket"
EXPORT_TASK_NAME="my-log-export"
START_TIME=$(date -d '1 day ago' +%s)
END_TIME=$(date +%s)

aws logs create-export-task \
    --log-group-name $LOG_GROUP_NAME \
    --from $START_TIME \
    --to $END_TIME \
    --destination $S3_BUCKET \
    --destination-prefix $EXPORT_TASK_NAME
