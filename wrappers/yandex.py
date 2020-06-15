# UNTESTED

import requests
import key_getter

url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'

def translate(text, source, dest):
    body_params = {
        "sourceLanguageCode": source,
        "targetLanguageCode": dest,
        "format": "PLAIN_TEXT",
        "texts": [
            text
        ],
        "folderId": "string"   # <- ??; also how to authenticate?
    }
    response = requests.request("POST", url=url, params=body_params)
    
    import pdb
    pdb.set_trace()
