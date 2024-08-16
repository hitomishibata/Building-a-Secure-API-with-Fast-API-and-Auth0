import requests
from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def access_protected_api():
    access_token=requests.session.get("user").get("access_token")
    url=f"{env.get("API_URL")}/api/messages/protected"
    if access_token is None:
        headers = {}
    else:
        headers ={
            "content-type": "application/json",
            "authorization": f"Bearer {access_token}"
            }
    res = requests.get(url, headers=headers)
    return res.json()

    
