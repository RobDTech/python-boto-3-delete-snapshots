import boto3 
import datetime
import pytz

client = boto3.client('ec2') 
ec2 = boto3.resource('ec2')
snapshots = client.describe_snapshots(OwnerIds=['self'])
count = 0
skipped = 0
for snap in snapshots["Snapshots"]: 
    if (snap["StartTime"]< datetime.datetime(2020,3,10).replace(tzinfo=pytz.UTC)):
        print(snap["StartTime"])
        
        try:
            ec2.Snapshot(snap["SnapshotId"]).delete()
            count = count + 1
            print("Deleted")
        except Exception as e:
            skipped = skipped + 1
            print(str(e))
            pass
print("Skipped : " + str(skipped))        
print("Done : " + str(count))
