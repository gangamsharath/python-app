'''Manageing IAM users and playing around'''
import boto3
iam=boto3.client('iam')
response=iam.create_user(UserName='murthy')
print(response)

users=iam.get_paginator('list_users')
print(users)

print(users.paginate())

for resp in users.paginate():
    print(resp)

iam.update_user(UserName='murthy',NewUserName="sriram")
iam.delete_user(UserName='sriram')


#using python with boto3 module
#i can manage s3,EC2,iam