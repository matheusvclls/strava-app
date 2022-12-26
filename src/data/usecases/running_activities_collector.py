from typing import Dict, List, Type
from src.domain.usecases import RunningListCollectorInterface
from src.data.interfaces.strava_api_consumer import StravaApiConsumerInterface

class StravaListCollector(RunningListCollectorInterface):
    ''' StravaListCollector usecase '''

    def __init__(self, api_consumer: Type[StravaApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:

        api_response = self.__api_consumer.get_activities(page)
        activities_formated_list = self.__format_api_response(api_response.response)
        return activities_formated_list

    @classmethod
    def __format_api_response(cls, activities: List[Dict]) -> List[Dict]:
        
        activities_formated_list = []
        for activity in activities:
            if activity['type'] == 'Run':
                activities_formated_list.append(
                    {
                        "id": activity["id"],
                        "name": activity["name"],
                        "moving_time": activity["moving_time"],
                        "elapsed_time": activity["elapsed_time"],
                        "average_speed": activity["average_speed"],
                        "max_speed": activity["max_speed"],
                    }
                )
        return activities_formated_list