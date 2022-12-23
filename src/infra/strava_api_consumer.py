from typing import Dict, Tuple, Type
from collections import namedtuple
import os
import requests
from requests import Request
from dotenv import load_dotenv

load_dotenv()
token = os.environ["TOKEN"]

class StravaApiConsumer():

    ''' Class to consume strava api '''

    def __init__(self) -> None:
        self.get_athlete_info_response = namedtuple('GET_Athlete_Info', 'status_code request response')

    def get_athlete_info(self) -> Tuple[int, Type[Request], Dict]:
        '''
        Request athlete info    
        Args:
            None
        Returns
            Tuple with status_code, request, response attributes
        ''' 
        req = requests.Request(
            method='GET',
            url="https://www.strava.com/api/v3/athlete",
            headers={
            "Authorization": f"Bearer {token}",
        }
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if ((status_code >= 200) and (status_code <= 299)):
            return self.get_athlete_info_response(
                status_code=status_code, request=req, response=response.json()
            )


    def get_activities(self, page: int) -> Tuple[int, Type[Request], Dict]:
        '''
        Request activities by page    
        Args:
            None
        Returns
            Tuple with status_code, request, response attributes
        ''' 
        req = requests.Request(
            method='GET',
            url="https://www.strava.com/api/v3/athlete/activities",
            headers={
            "Authorization": f"Bearer {token}",
            },
            params={"page":page}

        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)
        status_code = response.status_code

        if ((status_code >= 200) and (status_code <= 299) and (len(response.json())>0)):
            return self.get_athlete_info_response(
                status_code=status_code, request=req, response=response.json()
            )
        if ((status_code >= 200) and (status_code <= 299) and (len(response.json())==0)):
            return self.get_athlete_info_response(
                status_code=status_code, request=req, response=response.json()
            )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        '''
        Create a session and send http request
        Args:
            req_prepared: request object with all params
        Returns:
            response: http response as it comes
        '''

        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
