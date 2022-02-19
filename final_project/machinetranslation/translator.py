import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('SYf91-xAapkwQdGUC6RXhRbuk3rW59fFgeenQltVYnLb')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/8025e9c2-daaa-4d18-8f2f-81d5f8749a63')

def english_to_french(english_text):
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
