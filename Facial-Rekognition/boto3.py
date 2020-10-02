import json
import boto3
import os

def lambda_handler(event, context):
    s3_bucket = boto3.resource('s3')
    bucket=s3_bucket.Bucket('aws-ml-ai-week4')
    for key in bucket.objects.all():
      if key.key.startswith(''):
            print(key.key)
    tail = os.path.split(key.key)[1]

    
    client = boto3.client("rekognition",aws_access_key_id='ASIASWFNJ2FOYR6H2ZQX',aws_secret_access_key='mc1vwDRFlt6/OM5tAUqiLcLBbQ152kDEimFMK3Pw',aws_session_token='FwoGZXIvYXdzEFsaDAmipAeS0LE4N0gk0yLXAavaa2/zjGJf+ngdP56P6a19yxySz4UsWeZVyriGVFZkqM5WAuW3DrzN/y6mhhbcpUkOxHpAzKgQdL1t+Gyp5Hm8Saj/uZp3xcOb5c8UPDRd3J8+MHetyu00qz3Wi1FKXILQDtaJ50JJCI9UQWD2PqqJKi7G0kgu6++tn2Lzop43Hlpt2LWyCs1Q32gCJm/2FOiExSZJ06fc/fJWlngSMckplKAiCrjaqwjnLIs6uu1TQpwyuWWBiZcqSjM8Ojl7EOm0E/36gNX9ovB6aIN1AR/b7vWbEaL2KLvD1vsFMi1+q4AiM1C3n9R9HNktfC+/fSdJynN9jnelD9JY7Lg5COcyATF5LC73Y6aKpxM=')
  
    response = client.detect_faces(Image ={"S3Object":{"Bucket":"aws-ml-ai-week4", "Name":tail}},Attributes=['ALL'])
    print(type(response))
    json_data = json.dumps(response)
    message = {
   'message': 'Execution started successfully!'
    }
  

    return {
    'statusCode': 200,
     'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
    
    

    'body': json.dumps(json_data)
    }
   
    
    
   
    
        
    

