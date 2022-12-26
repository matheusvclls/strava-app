from abc import ABC, abstractmethod
from typing import Type, Tuple, Dict
from requests import Request

class StravaApiConsumerInterface(ABC):
    ''' Api consumer Interface '''

    @abstractmethod
    def get_activities(self, page: int) -> Tuple[int, Type[Request], Dict]:
        ''' Must Implement '''
        raise Exception('Must implement get_activities')