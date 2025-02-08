'''Download files from aws bucket'''
import boto3
s3=boto3.client('s3')
s3.download_file('mynamebucket','todolist.zip','client_todolist.zip')

''' check the file in currrent drive'''
