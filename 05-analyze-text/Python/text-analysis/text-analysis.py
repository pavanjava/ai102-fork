from dotenv import load_dotenv
import os

# Import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
        cog_key = os.getenv('COG_SERVICE_KEY')

        # Create client using endpoint and key
        azureKeyCredential = AzureKeyCredential(cog_key)
        cogClient = TextAnalyticsClient(endpoint=cog_endpoint, credential=azureKeyCredential)


        # Analyze each text file in the reviews folder
        reviews_folder = '/Users/pavanmantha/Pavans/ai102-fork/05-analyze-text/Python/text-analysis/reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get language
            detectedLanguage = cogClient.detect_language(documents=[text])[0]
            print(detectedLanguage.primary_language.name)

            # Get sentiment
            sentimentAnalysis = cogClient.analyze_sentiment(documents=[text])[0]
            print(f"Sentiment: {sentimentAnalysis.sentiment}")

            # Get key phrases
            phrases = cogClient.extract_key_phrases(documents=[text])[0].key_phrases
            if len(phrases) > 0:
                print("\n Key Phrases:")
                for phrase in phrases:
                    print("\t{}".format(phrase))

            # Get entities
            entities = cogClient.recognize_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nEntities")
                for entity in entities:
                    print('\t{} ({})'.format(entity.text, entity.category))

            # Get linked entities
            entities = cogClient.recognize_linked_entities(documents=[text])[0].entities
            if len(entities) > 0:
                print("\nLinks")
                for linked_entity in entities:
                    print('\t{} ({})'.format(linked_entity.name, linked_entity.url))



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()