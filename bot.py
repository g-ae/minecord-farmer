import time
import requests
import json

countfight = 8   # chaque 40 secs
countchop = 12   # chaque 60 secs
url = ""
jsonD = {}

def retrieve_last_message():
    try:
        r = requests.get(f'{url}?limit=1', headers=headers)
        response = json.loads(r.text)
        verif(response[0]['content'])
        return response[0]
    except:
        print('The token or channel id is wrong. Stopping...')
        exit()

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
    requests.post(url, data={'content': message}, headers=headers)
    print(message)

if (__name__ == "__main__"):
    with open('./config.json') as jsonFile:
        jsonD = json.load(jsonFile)
        url = f'https://discord.com/api/v8/channels/{jsonD["channelId"]}/messages'
        headers = {
            'Authorization': jsonD["token"]
        }
    while True:
        send("m!m")
        retrieve_last_message()
        if countfight == 8:
            countfight = 0
            send("m!f")
            retrieve_last_message()
        else:
            countfight += 1
        
        if countchop == 12:
            countchop = 0
            send("m!c")
            retrieve_last_message()
        else:
            countchop += 1

        time.sleep(4.4)
