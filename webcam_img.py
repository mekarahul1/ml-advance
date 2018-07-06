# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:20:06 2018

@author: rahul
"""

import boto3
import sys
if __name__ == "__main__":
    maxResults=2
    collectionId='MyCollection'
	
    client=boto3.client('rekognition','us-west-2')
    bucket='openbucket12'
    fileName=['testrahul.jpeg','testother.jpeg']
    threshold = 90
    maxFaces=2
    for file in fileName:
        response=client.search_faces_by_image(CollectionId=collectionId,
                                    Image={'S3Object':{'Bucket':bucket,'Name':file}},
                                    FaceMatchThreshold=threshold,
                                    MaxFaces=maxFaces)
    
                                    
        faceMatches=response['FaceMatches']
    #    print(response)
        if not faceMatches:
            print ('face not matched with the faces in database')
            break
        print ('Matching faces')
        person_name = response['FaceMatches'][0]['Face']['ExternalImageId']
         
        for match in faceMatches:
                print ('His FaceId is :' + match['Face']['FaceId'])
                print ('Has a Similarity of: ' + "{:.2f}".format(match['Similarity']) + "%")
                if(int(match['Similarity'])>85):
                    print('Person in the images is '+person_name)
                else:
                    print('I am unable to detect your face from database')
        print("===================================================")