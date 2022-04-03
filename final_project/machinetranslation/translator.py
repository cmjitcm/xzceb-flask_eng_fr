from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('CN-tzuLczBk8dV3sAmXI0RQch2wj3TaPE9UyFnpESyVb')
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator) 
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(text2):
    """Function translates English to French"""
    frenchtranslation = language_translator.translate(text=text2, model_id='en-fr').get_result()
    text2 = frenchtranslation['translations'][0]['translation']
    return text2

def french_to_english(text1):
    """Function translates French to English"""
    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()
    text1 = englishtranslation['translations'][0]['translation']
    return text1
