import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = os.environ.get("WEBSERVER_URL")

def readValue(virtualPin : str)->any:
    r =  requests.get(f"{url}/get?{virtualPin}")
    return r.json()

def writeValue(virtualPin : str , value : any)->any:
    r =  requests.get(f"{url}/update?{virtualPin}={value}")
    if (r.ok):
        print(f"Successfully Wrote Value for {virtualPin} : {value}")
    return r.json()
