from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.validators.get_running_collector_validator import get_pagination_validator

from src.main.adapters import request_adapter
from src.main.composer.get_running_collector_composer import get_running_collector_composer

from src.presenters.errors.error_controller import handle_errors

strava_routes = APIRouter()

@strava_routes.get('/api/strava/')
def get_test_fast_api(request: RequestFastApi):
    print(request.query_params)
    return {'hello': 'world!'}

@strava_routes.get("/api/strava/list")
async def get_running_collector_list(request: RequestFastApi, page: int):

    response = None
    controller = get_running_collector_composer()
    
    try:
        get_pagination_validator(request)
        response = await request_adapter(request, controller.handler)

    except Exception as e:
        response = handle_errors(e)
    
    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )