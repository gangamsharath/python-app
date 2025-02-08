# import boto3
# s3=boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

#CORS configuration

import boto3
s3=boto3.client('s3')

#set the CORS configuration for the bucket

cors_configuration={
    'CORSRules':[{
        'AllowedHeaders':['Authorization'],
        'AllowedMethods':['GET','PUT'],
        'AllowedOrigins':['*'],
        'ExposeHeaders':['GET','PUT'],
        'MaxAgeSeconds':3000
    }]
}

s3.put_bucket_cors(Bucket='murthy3',CORSConfiguration=cors_configuration)
result=s3.get_bucket_cors(Bucket='murthy3')
print(result)

