from .strava_api_consumer import StravaApiConsumer

def test_get_activities():
    ''' Test get_athlete_info method '''

    strava_api_consumer = StravaApiConsumer()
    page=1
    get_activities_response = strava_api_consumer.get_activities(page=page)

    assert get_activities_response.request.method == 'GET'
    assert get_activities_response.request.url == 'https://www.strava.com/api/v3/athlete/activities'

    assert get_activities_response.status_code == 200
    assert len(get_activities_response.response) > 0
    assert isinstance(get_activities_response.response, list)


def test_get_activities_empty_list():
    ''' Test get_activities method when returns an empty list'''

    strava_api_consumer=StravaApiConsumer()
    page=200000

    get_activities_response = strava_api_consumer.get_activities(page=page)

    assert get_activities_response.response == []
        