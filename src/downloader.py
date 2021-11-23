import requests
from dotenv import load_dotenv
import os

BASE_ENDPOINT = 'http://api.511.org/transit/'

def download_data(api, **kwargs):
    load_dotenv()
    api_key=os.environ.get("api_key")
    endpoint = BASE_ENDPOINT + api + '?api_key=' + api_key
    return requests.get(endpoint)
