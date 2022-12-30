from src.presenters.controllers.running_activities_collector_controller import RunningListCollectorController
from src.data.usecases.running_activities_collector import StravaListCollector
from src.infra.strava_api_consumer import StravaApiConsumer

def get_running_collector_composer():
    ''' Composer '''

    infra = StravaApiConsumer()
    usecase = StravaListCollector(infra)
    controller = RunningListCollectorController(usecase)

    return controller