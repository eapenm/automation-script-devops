#!/bin/bash

USER="your-username"
NEW_ACCESS_KEY=$(aws iam create-access-key --user-name $USER | jq -r '.AccessKey')

# Store new access key safely (e.g., to Secrets Manager or a config file)
echo "New Access Key: $NEW_ACCESS_KEY"

# Once validated, deactivate the old key
OLD_ACCESS_KEY="old-access-key-id"
aws iam update-access-key --access-key-id $OLD_ACCESS_KEY --status Inactive --user-name $USER
