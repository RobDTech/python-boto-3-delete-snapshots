# python-boto-3-delete-snapshots
Removes snapshots not attached to an AMI and before a certain date

Requires boto3 and pytz.

pip install boto3

pip install pytz

Configure IAM permissions for EC2 Snapshots either through
1: aws configure
or
2: Attach IAM Role to EC2 
