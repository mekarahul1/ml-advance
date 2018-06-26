# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 17:36:49 2018

@author: rahul
"""
import boto3

if __name__ == "__main__":
    maxResults=2
    collectionId='MyCollection'
	
    client=boto3.client('rekognition','us-west-2')

    file=['rahul1.JPG','rahul2.JPG','rahul3.jpg','rahul4.jpg','rahul5.jpg']
    file2=['suraj1.JPG','suraj2.JPG','suraj3.JPG','suraj4.JPG','suraj5.JPG']
    bucket='openbucket12'
    for f in file:
            fileName=f
            
            response=client.index_faces(CollectionId=collectionId,
                                        Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                        ExternalImageId='Rahul',
                                        DetectionAttributes=['ALL'])
            #print(response)
            print ('Faces in ' + fileName) 							
            for faceRecord in response['FaceRecords']:
                 print (faceRecord['Face']['FaceId'])
    for f in file2:
            fileName=f
            
            response=client.index_faces(CollectionId=collectionId,
                                        Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                        ExternalImageId='Suraj',
                                        DetectionAttributes=['ALL'])
            #print(response)
            print ('Faces in ' + fileName) 							
            for faceRecord in response['FaceRecords']:
                 print (faceRecord['Face']['FaceId'])    
    fileName='testimage.jpg'
    threshold = 90
    maxFaces=2
  
    response=client.search_faces_by_image(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print(response)
    print ('Matching faces')
    person_name = response['FaceMatches'][0]['Face']['ExternalImageId']
    print('Person in the images is '+person_name)
    for match in faceMatches:
            print ('His FaceId is :' + match['Face']['FaceId'])
            print ('Has a Similarity of: ' + "{:.2f}".format(match['Similarity']) + "%")
            print ()
