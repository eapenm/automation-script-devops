#!/bin/bash

LOG_DIR="/var/log/myapp"
RETENTION_DAYS=7

find $LOG_DIR -type f -mtime +$RETENTION_DAYS -exec rm -f {} \;
