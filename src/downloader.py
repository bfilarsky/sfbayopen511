import requests
from dotenv import load_dotenv
import os

__BASE_ENDPOINT = 'http://api.511.org/transit/'


def createEndpoint(api, api_key, **kwargs):
    endpoint = __BASE_ENDPOINT + api + '?api_key=' + api_key
    for key, value in kwargs.items():
        endpoint = endpoint + '&' + key + '=' + value
    return endpoint


def downloadData(endpoint):
    data = requests.get(endpoint)
    if (data.status_code == 200):
        return data.text
    else:
        return None


def getApiKey():
    load_dotenv()
    return os.environ.get("api_key")


def downloadJSON(api, **kwargs):
    kwargs['api_key'] = getApiKey()
    kwargs['format'] = 'json'
    endpoint = createEndpoint(api, **kwargs)
    return downloadData(endpoint)
