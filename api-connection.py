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

def get_activity_by_id(activity_id : int):
    response = requests.get(
        f"{BASE_URL}/activities/{activity_id}",
        headers={
            "Authorization": f"Bearer {token}",
        }
    )
    return response

def get_athlete_stats(athlete_id : int):
    response = requests.get(
        f"{BASE_URL}/athletes/{athlete_id}/stats",
        headers={
            "Authorization": f"Bearer {token}",
        }
    )
    return response

def refresh_token():
    response = requests.post(
        f"https://www.strava.com/oauth/token",
        
        params={
        "client_id":os.environ['CLIENT_ID']
        ,"client_secret":os.environ['CLIENT_SECRET']
        ,"grant_type":"refresh_token"
        ,"refresh_token":os.environ['refresh_token']
        }
    )
    return response


#print(get_activities({"page":"3"}).json())
#print(get_athlete_stats(6115740).json())
#print(refresh_token().json())