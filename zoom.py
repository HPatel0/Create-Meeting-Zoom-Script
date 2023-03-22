import jwt
import requests
import json
from time import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# API key/secret key and userId from zoom API
API_KEY = os.environ.get("APIKEY")
API_SEC = os.environ.get("APISECRET")
userId = os.environ.get("USERID")

# create a function to generate a token using the pyjwt library
def generateToken():
    token = jwt.encode(
        # Create a payload of the token containing API Key & expiration time
        {'iss': API_KEY, 'exp': time() + 5000},
        API_SEC,
        algorithm='HS256'
    )
    return token
    # send a request with headers including a token

# gets data of user
def getUsers():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}

    r = requests.get('https://api.zoom.us/v2/users/', headers=headers)
    print(r.text)


meetingdetails = {"topic": "test for python zoom script",
                  "type": 2,
                  "duration": "40",
                  "timezone": "America/New_York",
                  "agenda": "test",
                  "recurrence": {"type": 1,
                                 "repeat_interval": 1
                                 },
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "False",
                               "mute_upon_entry": "True",
                               "watermark": "true",
                               "audio": "voip",
                               "auto_recording": "cloud"
                               }
                  }

def createMeeting():
    headers = {'authorization': 'Bearer %s' % generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/{userId}/meetings', headers=headers, data=json.dumps(meetingdetails))
    print(r.text)

getUsers()
createMeeting()
print("------------------------------------")
print("Successful creation of zoom meeting!")
