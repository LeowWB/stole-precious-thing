import requests
import key_getter

url = "https://microsoft-azure-microsoft-text-translation-3-0-v1.p.rapidapi.com/translate"

headers = {
    'x-rapidapi-host': "microsoft-azure-microsoft-text-translation-3-0-v1.p.rapidapi.com",
    'x-rapidapi-key': key_getter.get_key('microsoft'),
    'content-type': "application/json",
    'accept': "application/json"
    }

def translate(text, source, dest):
    querystring = {"from":source,"to":dest,"api-version":"3.0"}
    payload = '[{"Text":"' + text + '"}]'
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response.json()[0]['translations'][0]['text']
