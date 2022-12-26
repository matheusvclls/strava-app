from abc import ABC, abstractmethod
from typing import Dict, List

class RunningListCollectorInterface(ABC):
    ''' Activities Collector Interface '''

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        ''' Must implement '''
        raise Exception('Must implement list method')