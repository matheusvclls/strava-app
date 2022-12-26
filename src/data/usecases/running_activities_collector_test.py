from src.infra.strava_api_consumer import StravaApiConsumer
from .running_activities_collector import StravaListCollector

def test_list():

    api_consumer = StravaApiConsumer()
    running_list_colector = StravaListCollector(api_consumer)

    page = 1
    response = running_list_colector.list(page=page)
    #print(response)
    assert isinstance(response, list)
    assert "id" in response[0]
