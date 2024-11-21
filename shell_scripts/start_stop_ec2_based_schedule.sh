#!/bin/bash

INSTANCE_ID="i-xxxxxx"
ACTION=$1  # Start or Stop

if [ "$ACTION" == "start" ]; then
    aws ec2 start-instances --instance-ids $INSTANCE_ID
elif [ "$ACTION" == "stop" ]; then
    aws ec2 stop-instances --instance-ids $INSTANCE_ID
else
    echo "Invalid action. Use 'start' or 'stop'."
fi
