'How to manage ws ec2 key pairs'
import boto3
ec2=boto3.client('ec2')
response=ec2.describe_key_pairs()
print(response)


ec2.describe_key_pairs()
result=ec3.create_key_pair(KeyName='NEWKEY')
print(result)

ec2.delete_key_pair(KeyName='NEWKEY')
ec2.describe_key_pairs()
ec2.delete_key_pair(KeyName='aws-eb')
ec2.describe_key_pairs()