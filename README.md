 Multi-Region S3 Replication with Data Integrity Check:
 This script replicates objects between S3 buckets in two different regions and verifies data integrity with checksums.

 EC2 Auto-Recovery with CloudWatch Alarms (Python)
This script triggers EC2 instance recovery when certain metrics (like CPU or Network) breach predefined CloudWatch thresholds.

Automated RDS Snapshot Cleanup Based on Retention Policy (Python)
This script automatically deletes old RDS snapshots based on a defined retention policy (e.g., retain the last 7 days).

Automated Compliance Monitoring for Security Groups (Python)
This script continuously monitors AWS security groups and automatically removes rules that violate predefined security policies.

 Auto-Scaling EKS Worker Nodes Based on SQS Queue Length (Python)
This script dynamically scales EKS worker nodes based on the length of an SQS queue, ensuring that the Kubernetes cluster has enough capacity to process jobs.

Start and Stop EC2 Instances Based on Schedule (Python)
Automatically start or stop EC2 instances based on a schedule (e.g., stop instances at night and start them in the morning).

Monitor S3 Bucket for Unused Objects and Delete Them (Python)
Script to delete objects in an S3 bucket that haven’t been accessed for a long time.
Automatically Take EBS Snapshots for Backup (Python)
This script will automatically take snapshots of all EBS volumes attached to EC2 instances for backup purposes.

AWS Lambda to Auto Scale Based on CloudWatch Metrics (Python)
A Lambda function to automatically increase EC2 instances when CPU utilization crosses a threshold.

Create an IAM Role with Policies (Python)
A script to create an IAM role and attach a policy to allow S3 access.



Shell files:

S3 Bucket Versioning and Lifecycle Policy Automation (Shell)
Enable versioning on an S3 bucket and set a lifecycle policy to move objects to Glacier after 30 days.

Continuous Monitoring of SSL Certificate Expiration (Shell)
Monitor SSL certificate expiration across multiple domains and notify when expiration is approaching.
Automated EBS Volume Expansion for EC2 Instances (Shell)
Monitor EBS volume usage and automatically expand volumes when usage exceeds 80%.

AWS Lambda Deployment Automation with ZIP Creation (Shell)
Automate the packaging and deployment of AWS Lambda functions with dependencies.

Auto-Rotate IAM Access Keys (Shell)
Rotate IAM access keys and deactivate old ones after the new key has been confirmed working.

Automate CloudWatch Logs Export to S3 (Shell)
This script exports CloudWatch logs to an S3 bucket.
Rotate Logs in EC2 Instances (Shell)
A script to rotate logs in a specific directory and delete logs older than a specified number of days.

Check EC2 Instance Health Status (Shell)
This script checks the health status of all EC2 instances.

Automated S3 Backup Script (Shell)
Backup files from a local directory to an S3 bucket.

Start and Stop EC2 Instances (Shell)
This script will stop and start EC2 instances by instance ID using the AWS CLI.