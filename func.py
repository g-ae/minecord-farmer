import requests
import json

with open('./config.json') as jsonFile:
    jsonD = json.load(jsonFile)
    url = f'https://discord.com/api/v8/channels/{jsonD["channelId"]}/messages'
    headers = {
        'Authorization': jsonD["token"]
    }

def retrieve_last_message():
    try:
        r = requests.get(f'{url}?limit=1', headers=headers)
        response = json.loads(r.text)
        verif(response[0]['content'])
        return response[0]
    except:
        err()

def verif(content):
    if "Anti bot check" in content:
        verif = content[content.find('`')+1:content.find('`.\n')]
        send(f'm!verify {eval(verif)}')
    elif "Please complete the verification first" in content:
        completeVerif()

def completeVerif():
    try:
        r = requests.get(f'{url}?limit=10', headers=headers)
        response = json.loads(r.text)
        for value in response:
            if "Anti bot check" in value['content']:
                verif(value['content'])
                break
    except:
        err()

def send(message):
    try:
        requests.post(url, data={'content': message}, headers=headers)
        print(message)
    except:
        err()

def err():
    print('The token or channel id is wrong.')
    exit()