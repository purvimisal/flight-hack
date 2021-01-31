import json
import requests 

with open('messages.json') as fp:
    MESSAGES = json.load(fp)

def get_message(event):
    if event in MESSAGES.keys():
        image = MESSAGES[event]['Image']
        text =  MESSAGES[event]['Text']
        detailed_image = MESSAGES[event]['Detailed_Image']
        link = MESSAGES[event]['Link']

        return {
            'image': image,
            'text' : text,
            'detailed_image':detailed_image,
            'link': link
        }
    else:
        return False



