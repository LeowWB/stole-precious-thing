import requests
import key_getter
import urllib

url = "https://nlp-translation.p.rapidapi.com/v1/translate"
headers = {
    'x-rapidapi-host': "nlp-translation.p.rapidapi.com",
    'x-rapidapi-key': key_getter.get_key('nlp_gofitech'),
    'content-type': "application/x-www-form-urlencoded"
}

def translate(text, source, dest):
    payload = f"from={source}&text={urllib.parse.quote(text)}&to={dest}"
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['translated_text'][dest]
