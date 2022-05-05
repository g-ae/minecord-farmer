from sys import prefix
import time
import requests
import json

countfight = 8   # every ~40 seconds
countchop = 12   # every ~60 seconds
url = ""
jsonD = {}
prefix = ""

# Get last message sent in the channel
def retrieve_last_message():
    try:
        r = requests.get(f'{url}?limit=1', headers=headers)
        response = json.loads(r.text)
        verif(response[0]['content'])
        return response[0]
    except:
        print('The token or channel id is wrong. Stopping...')
        exit()

# Check for anti bot verification
def verif(content):
    if "Anti bot check" in content:
        verif = content[content.find('`')+1:content.find('`.\n')]
        send(f'{prefix}verify {eval(verif)}')
    elif "Please complete the verification first" in content:
        completeVerif()

# Used if the verification message has already passed so you need to check for recent messages
def completeVerif():
    r = requests.get(f'{url}?limit=10', headers=headers)
    response = json.loads(r.text)
    for value in response:
        if "Anti bot check" in value['content']:
            verif(value['content'])
            break

# Send a message in the channel provided in config.json
def send(message):
    requests.post(url, data={'content': message}, headers=headers)
    # logs the sent message in the terminal so you can check if you need
    print(message) # you can't comment this line if you don't want anything in your console. (put a # at the start of the line)

# Will only execute if used directly
if (__name__ == "__main__"):
    with open('./config.json') as jsonFile:
        jsonD = json.load(jsonFile)
        prefix = jsonD["prefix"]
        url = f'https://discord.com/api/v8/channels/{jsonD["channelId"]}/messages' # API version can be updated (check Discord's documentation to see if sending messages will still work)
        headers = {
            'Authorization': jsonD["token"]
        }
    while True:
        send(f"{prefix}m")
        retrieve_last_message()
        if countfight == 8:
            countfight = 0
            send(f"{prefix}f")
            retrieve_last_message()
        else:
            countfight += 1
        
        if countchop == 12:
            countchop = 0
            send(f"{prefix}c")
            retrieve_last_message()
        else:
            countchop += 1

        time.sleep(5) # every 5 seconds for safety (you can reduce it down to 4.4 and it should keep working like normal)
