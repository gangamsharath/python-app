'How to create AWS EC2 instance'
'we can start,stop and montor instance from boto3'

import boto3
ec2=boto3.client('ec2')
response=ec2.describe_instances()
print(response)  

result=ec2.monitor_instance(InstanceIds=['1-33344422xxx'])
' copy instanceID from AWS resource group and paste above'

result=ec2.unmonitor_instance(InstanceIds=['1-3334444xxx'])
print(result)

ec2.stop_instance(InstanceIds=['1-333444xxxxxx'])

ec2.reboot_instances(InstanceIds=['1-333444cxxxxx'])

