# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 12:21:13 2018

@author: rahul
"""

import boto3
import json
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text1 = ["It is raining today in Seattle","I feel great this morning.","This view is horrible","Childhood is the time to play","I love Seattle but the winter is too cold for me."]
for text in text1:
        print("for text  :"+text)
        print('Calling DetectEntities')
        print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
        print('Calling DetectDominantLanguage')
        print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))
        print('Calling DetectSentiment')
        print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
        print('Calling DetectKeyPhrases')
        print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
