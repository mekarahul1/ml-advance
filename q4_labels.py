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
            'Name': "mountains.jpeg", # image has a mountain
        },
    },
    MaxLabels=123,
    MinConfidence=90,
)
response2 = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': "imagesofme",
            'Name': "group.jpg", # image has  10 people
        },
    },
    MaxLabels=123,
    MinConfidence=90,
)

response3 = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': "imagesofme",
            'Name': "rahul1.jpg",  # image has a face
        },
    },
    MaxLabels=123,
    MinConfidence=90,
)

#print(response['Labels'])
k=response['Labels']
c=0
c1=0
c2=0
k2=response2['Labels']
k3=response2['Labels']
for i in range(len(k)):
    if(k[i]['Name']=='Mountain'):
        print("Montain object is present in image")
        c=c+1;
        break;
        
if(c==0):
    print("object not found")

for i in range(len(k2)):
    if(k2[i]['Name']=='Mountain'):
        print("for 2nd image Montain object is present in image")
        c1=c1+1;
        break;
        
if(c1==0):
    print("object not found")

for i in range(len(k3)):
    if(k3[i]['Name']=='Mountain'):
        print("for 2nd image Montain object is present in image")
        c2=c2+1;
        break;
        
if(c2==0):
    print("object not found")
