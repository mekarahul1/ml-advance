# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:38:51 2018

@author: rahul
"""
# object is Mountain
import boto3
rekognition = boto3.client("rekognition", "us-west-2")
response = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': "imagesofme",
            'Name': "mountains.jpeg",
        },
    },
    MaxLabels=123,
    MinConfidence=90,
)

#print(response['Labels'])
k=response['Labels']
c=0
for i in range(len(k)):
    if(k[i]['Name']=='Mountain'):
        print("Montain object is present in image")
        c=c+1;
        break;
        
if(c==0):
    print("object not found")