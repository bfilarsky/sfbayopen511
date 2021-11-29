import requests
import json

__BASE_ENDPOINT = 'http://api.511.org/transit/'


def createEndpoint(api, api_key, **kwargs):
    endpoint = __BASE_ENDPOINT + api + '?api_key=' + api_key
    for key, value in kwargs.items():
        endpoint = endpoint + '&' + key + '=' + value
    return endpoint


def downloadData(endpoint):
    data = requests.get(endpoint)
    data.encoding = 'utf-8-sig'
    if (data.status_code == 200):
        return data.text
    else:
        return None


def download(api, api_key, **kwargs):
    kwargs['format'] = 'json'
    endpoint = createEndpoint(api, api_key, **kwargs)
    return json.loads(downloadData(endpoint))
