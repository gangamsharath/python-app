' Bucket policies'

import boto3
s3=boto3.client('s3')
result=s3.get_bucket_policy(Bucket='mynamebucket')

bucket_policy={ 
    'Version':'2020-06-15',
    'Statement':[
        {
            'Sid':'AddPerm',
            'Effect':'Allow',
            'Principal':'*',
            'Action':['s3.GetObject'],
            'Resource':"arn:aws:s3:%s/*" % 'mynamebucket'
        }
    ]
}

import json
bucket_policy=json.dumps(bucket_policy)

'Now set the policy'
s3.put_bucket_policy(Bucket='mynamebucket',policy=bucket_policy)
bucket_policy=json.dumps(bucket_policy)



