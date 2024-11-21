#!/bin/bash

aws ec2 describe-instance-status --query 'InstanceStatuses[*].{Instance:InstanceId,Status:InstanceStatus.Status}' --output table
