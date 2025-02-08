''' Download with exception handling'''

import boto3
import botocore3
s3=boto3.resource('s3')
try:
    s3.Bucket('mynamebucket').download_file('todolist.zip','client_todolist.zip')
except botocore3.exceptions.ClientErrors as e:
    print('No object in AWS bucket')
