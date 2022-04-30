#!/usr/bin/env python3
import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###

kwargs={
    "Text":"I am learning programming in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"it"
    }

def main():
    translate_text(**kwargs)

if __name__=="__main__":
    main()


