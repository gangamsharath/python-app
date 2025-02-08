''' Creating new bucket and upload files'''

import boto3
s3=boto3.client('s3')
response=s3.list_buckets()
print(response)

buckets=[bucket['Name'] for bucket in response['Buckets']]
print ('Bucket name :%s' % buckets)

'''new bucket'''
s3.create_bucket(Bucket='newbucket',
                  CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})

'upload file now'
filename='mytodolist.zip'
bucket_name='mynamebucket'
s3.upload_file(filename,bucket_name)

' Now check in aws  for new file which is uploaded'