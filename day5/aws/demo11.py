''' Creating IAM access Keys for the user'''

import boto3
iam=boto3.client('iam')
response=iam.create_access_key(UserName='newuser')
print(response)

''' now using this access key, user can perform operations programmatically'''

