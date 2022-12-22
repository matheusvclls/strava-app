from dotenv import load_dotenv
import os
import requests

load_dotenv()
BASE_URL = "https://www.strava.com/api/v3"
token = os.environ["TOKEN"]

def get_athlete_info():
    response = requests.get(
        f"{BASE_URL}/athlete",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )
    return response

def get_activities(payload={}):
    response = requests.get(
        f"{BASE_URL}/athlete/activities",
        headers={
            "Authorization": f"Bearer {token}",
        },
        params=payload
    )
    return response


print(get_activities({"page":"3"}).json())
