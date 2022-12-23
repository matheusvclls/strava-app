from .strava_api_consumer import StravaApiConsumer

def test_get_athlete_info():
    ''' Test get_athlete_info method '''

    strava_api_consumer = StravaApiConsumer()

    get_athlete_info_response = strava_api_consumer.get_athlete_info()

    assert get_athlete_info_response.request.method == 'GET'
    assert get_athlete_info_response.request.url == 'https://www.strava.com/api/v3/athlete'

    assert get_athlete_info_response.status_code == 200
    assert isinstance(get_athlete_info_response.response, dict)
