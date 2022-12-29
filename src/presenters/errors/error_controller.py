from typing import Type, Dict
from src.errors import HttpRequestError, HttpUnprocessableEntityError

def handle_errors(error: Type[Exception]) -> Dict:
    if isinstance(error, HttpRequestError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
        }
    elif isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
        }
    else:
        return {
            "data": { "error": str(error) },
            "status_code": 500
        }