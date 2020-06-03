import json

def get_key(api):
    with open('./keys.json', 'r') as file:
        return json.load(file)[api]
