import requests
import json

token = "token"             # write own discord token
channelid = "channel id";   # id of the channel where you'll be executing this
url = f'https://discord.com/api/v8/channels/{channelid}/messages'
headers = {
    'Authorization': token
}

def retrieve_last_message():
    r = requests.get(f'{url}?limit=1', headers=headers)
    response = json.loads(r.text)
    verif(response[0]['content'])
    return response[0]

def verif(content):
    if "Anti bot check" in content:
        verif = content[content.find('`')+1:content.find('`.\n')]
        send(f'm!verify {eval(verif)}')
    elif "Please complete the verification first" in content:
        completeVerif()

def completeVerif():
    r = requests.get(f'{url}?limit=10', headers=headers)
    response = json.loads(r.text)
    for value in response:
        if "Anti bot check" in value['content']:
            verif(value['content'])
            break

def send(message):
    payload = {
        'content': message
    }
    r = requests.post(url, data=payload, headers=headers)
    print(message)