'Using  Elastic IP address in Amazon EC2'
import boto3
ec2=boto3.client('ec2')

print(ec2)   
filters=[ { 'Name':'domain','Values':['vpc']}]
reponse=ec2.describe_addresses(Filters=filters)
print(response)

allocation=ec2.allocate_address(Domain='vpc')
response=ec2.assocate_address(AllocationId='xxxx',InstanceId='i-030xx')
print(allocation)
print(response)

response=ec3.release_address(AllocationId='i-030xxx')
print(response)

