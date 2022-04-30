#!/usr/bin/env python3
import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    return(response) # this code is inside the function and will print the contents of the variable 'response'

def main():
    print(translate_text())
    

if __name__=="__main__":
    main()