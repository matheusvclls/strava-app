from fastapi import APIRouter, Request as RequestFastApi

strava_routes = APIRouter()

@strava_routes.get('/api/strava/test')
def get_test_fast_api(request: RequestFastApi):
    print(request.query_params)
    return {'hello': 'world!'}