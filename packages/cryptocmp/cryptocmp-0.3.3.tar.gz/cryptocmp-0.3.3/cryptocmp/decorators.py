from functools import wraps

import requests

from cryptocmp import URL_BASE
from cryptocmp.exceptions import CryptoCompareException


def extract_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        data = response['Data']
        return data
    return wrapper


def response_error_raise(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if 'Response' in response and response['Response'] == 'Error':
            raise CryptoCompareException(response)
        return response
    return wrapper


def get(path):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            params = func(*args, **kwargs)
            response = requests.get(URL_BASE + path, params=params)
            return response.json()
        return wrapper
    return decorator
