from dotenv import load_dotenv
import os
import json
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main():
    global cog_endpoint
    global cog_key

    try:
        # Get Configuration Settings
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Get user input (until they enter "quit")
        userText =''
        while userText.lower() != 'quit':
            userText = input('\nEnter some text ("quit" to stop)\n')
            if userText.lower() != 'quit':
                result = GetLanguage(userText)
                print('Language:', result)

    except Exception as ex:
        print(ex)

def GetLanguage(text):

    # Create client using endpoint and key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)

    # Call the service to get the detected language
    detectedLanguage = client.detect_language(documents = [text])[0]
    return detectedLanguage # gives almost the same details as json response compared to rest-client.py code but in the python object format
    # we can return the exact language by replace the above return with the below return statement
    # return detectedLanguage.primary_language.name


if __name__ == "__main__":
    main()