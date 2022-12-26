from fastapi import APIRouter, Request as RequestFastApi

strava_routes = APIRouter()

@strava_routes.get('/api/strava/list')
def get_running_in_pagination(request: RequestFastApi):
    print(request.query_params)
    return {'hello': 'world!', 'params':request.query_params}