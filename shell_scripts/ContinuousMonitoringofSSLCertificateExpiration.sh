#!/bin/bash

DOMAINS=("example.com" "anotherdomain.com")
DAYS_THRESHOLD=30

for DOMAIN in "${DOMAINS[@]}"; do
    EXPIRATION_DATE=$(echo | openssl s_client -servername $DOMAIN -connect $DOMAIN:443 2>/dev/null | openssl x509 -noout -enddate | sed 's/notAfter=//')
    EXPIRATION_SECS=$(date --date="$EXPIRATION_DATE" +%s)
    CURRENT_SECS=$(date +%s)
    DIFF_DAYS=$(( ($EXPIRATION_SECS - $CURRENT_SECS) / 86400 ))

    if [ $DIFF_DAYS -le $DAYS_THRESHOLD ]; then
        echo "SSL certificate for $DOMAIN expires in $DIFF_DAYS days!"
    fi
done
