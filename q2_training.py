# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:15:45 2018

@author: rahul
"""

import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('rahul1.JPG','meka rahul'),
      ('rahul2.JPG','meka rahul'),
      ('rahul3.jpg','meka rahul'),
      ('rahul4.jpg','meka rahul'),
      ('rahul5.jpg','meka rahul'),
      ('suraj1.JPG','suraj'),
      ('suraj2.JPG','suraj'),
      ('suraj3.JPG','suraj'),
      ('suraj4.JPG','suraj'),
      ('suraj5.JPG','suraj')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('openbucket12','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )