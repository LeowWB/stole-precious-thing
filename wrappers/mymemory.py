# there's no space in the name (MyMemory)

import requests
import key_getter

url = "https://translated-mymemory---translation-memory.p.rapidapi.com/api/get"

headers = {
    'x-rapidapi-host': "translated-mymemory---translation-memory.p.rapidapi.com",
    'x-rapidapi-key': key_getter.get_key('mymemory')
    }

def translate(text, source, dest):
    querystring = {
        "mt":"1",
        "onlyprivate":"0",
        "de":key_getter.get_key('mymemory_email'),
        "langpair":f"{source}|{dest}",
        "q":text
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['responseData']['translatedText']
