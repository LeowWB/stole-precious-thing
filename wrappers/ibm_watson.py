import json
import key_getter
import requests
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def translate(text, source, dest):
    authenticator = IAMAuthenticator(key_getter.get_key('ibm_key'))
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(key_getter.get_key('ibm_url'))

    translation = language_translator.translate(
        text=text,
        model_id=f'{source}-{dest}').get_result()

    return translation['translations'][0]['translation']
    
import pdb
pdb.set_trace()
