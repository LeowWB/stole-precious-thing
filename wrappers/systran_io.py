import requests
import key_getter

url = "https://systran-systran-platform-for-language-processing-v1.p.rapidapi.com/translation/text/translate"

headers = {
    'x-rapidapi-host': "systran-systran-platform-for-language-processing-v1.p.rapidapi.com",
    'x-rapidapi-key': key_getter.get_key('systran_io')
}

def translate(text, source, dest):
    querystring = {"source":source,"target":dest,"input":text}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['outputs'][0]['output']
