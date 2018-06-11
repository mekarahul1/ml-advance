# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 17:39:01 2018

@author: rahul
"""

from boto3 import  client
import boto3
from io import StringIO
#import StringIO
from contextlib import closing

polly = client("polly", 'us-east-1' )
usertext=input("enter the text ");
response = polly.synthesize_speech(
    Text="The text you entered is "+usertext,
    OutputFormat="mp3",
    VoiceId="Raveena")

print(response)

if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        data = stream.read()
        fo = open("pollytest.mp3", "wb")
        fo.write(data)
        fo.close()