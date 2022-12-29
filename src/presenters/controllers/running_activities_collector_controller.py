from typing import Dict
from src.domain.usecases.running_collector import RunningListCollectorInterface
from src.presenters.interface.controllers import ControllersInterface

class RunningListCollectorController(ControllersInterface):
    ''' Controller to List Running Activities '''

    def __init__(self, running_list_collector: RunningListCollectorInterface) -> None:
        self.__use_case = running_list_collector

    def handler(self, http_request: Dict):
        ''' Handler to list colector '''

        page = http_request["query_params"]["page"]

        running_list = self.__use_case.list(page)
        http_response = { "status_code": 200, "data": { "data": running_list } }

        return http_response