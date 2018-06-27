# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:42:03 2018

@author: rahul
"""

import cv2
import boto3

video=cv2.VideoCapture(0)
check, frame = video.read()
cv2.imshow("Color Frame",frame)


if __name__ == "__main__":
    client=boto3.client('rekognition', region_name='us-west-2')    
    response = client.detect_labels(Image={'Bytes': cv2.imencode('.jpg', frame)[1].tobytes()},MinConfidence=50)
		
    print('Detected labels')
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

cv2.waitKey(0)
cv2.destroyAllWindows()