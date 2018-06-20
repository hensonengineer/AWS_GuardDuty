#GuardDutyAutoStopInstances
#change region in line 17
#change timeout in Lambda to 15 seconds

import boto3
import json


def lambda_handler(event, context):
    
     print('loading handler')
     result = json.dumps(event)
     instanceId = event['detail']['resource']['instanceDetails']['instanceId']
     type = event['detail']['description']


     ec2 = boto3.client('ec2', region_name = 'us-west-2')
     ec2.create_tags(Resources=[instanceId], Tags=[{'Key':'Name', 'Value':'DANGER - DO NOT RESTART - COMPROMISED'}])
     ec2.stop_instances(InstanceIds = [instanceId])
     
     return
     