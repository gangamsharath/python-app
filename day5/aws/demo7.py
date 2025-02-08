'Web site hosting configuraton'
import boto3
s3=boto3.client('s3')
web={
    'ErrorDocument':{
        'Key':'error.html',
        'IndexDocument':{'suffix':'index.html'}
    }
}

s3.put_bucket_website(Bucket='mynamebucket',WebSiteConfiguration=web)
result=s3.get_bucket_website(Bucket='mynamebucket')
print(result)

'in aws, oberve error.html and index.html'

'Create index.html and write code. now upload to  website'

s3.upload_file('index.html','mynamebucket','index.html')