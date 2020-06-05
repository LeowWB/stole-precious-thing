import requests
import key_getter
import urllib.parse

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': key_getter.get_key('google_translate'),
    'accept-encoding': "application/gzip",
    'content-type': "application/x-www-form-urlencoded"
    }

def translate(text, source, dest):
    payload = f"source={source}&q={urllib.parse.quote(text)}&target={dest}"
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['data']['translations'][0]['translatedText']
