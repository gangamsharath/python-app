import boto3

# Initialize a session using Amazon WAF
client = boto3.client('wafv2', region_name='us-east-1')

# Create a WAF Web ACL
response = client.create_web_acl(
    Name='murthy',
    Scope='REGIONAL',  # Change to 'CLOUDFRONT' if needed
    DefaultAction={
        'Allow': {}
    },
    Description='WAF Web ACL named murthy',
    VisibilityConfig={
        'SampledRequestsEnabled': True,
        'CloudWatchMetricsEnabled': True,
        'MetricName': 'murthyMetric'
    },
    Rules=[],
    Tags=[]
)

print(response)