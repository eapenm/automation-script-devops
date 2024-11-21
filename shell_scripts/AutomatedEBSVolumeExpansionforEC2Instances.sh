#!/bin/bash

INSTANCE_ID="i-xxxxxx"
VOLUME_ID=$(aws ec2 describe-volumes --filter "Name=attachment.instance-id,Values=$INSTANCE_ID" --query "Volumes[*].VolumeId" --output text)

# Get current volume size
CURRENT_SIZE=$(aws ec2 describe-volumes --volume-id $VOLUME_ID --query "Volumes[*].Size" --output text)

# If size is above 80%, expand the volume by 20%
THRESHOLD=80
USAGE=$(df -h /dev/nvme1n1p1 | grep -v Filesystem | awk '{print $5}' | sed 's/%//')

if [ $USAGE -ge $THRESHOLD ]; then
    NEW_SIZE=$((CURRENT_SIZE + 20))
    aws ec2 modify-volume --volume-id $VOLUME_ID --size $NEW_SIZE
    echo "Volume expanded to $NEW_SIZE GB."
fi
