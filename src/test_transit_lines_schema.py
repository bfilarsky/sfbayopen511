from jsonschema import validate
import json
from dotenv import load_dotenv
import os

from downloader import download


def test_nominal_schema():
    with open('test_data/lines_schema.json') as schema, open('test_data/lines_nominal.json') as nominal:
        validate(instance=json.load(nominal), schema=json.load(schema))


def test_live_schema():
    load_dotenv()
    api_key = os.environ.get("api_key")
    transit_lines_live = download('lines', api_key, operator_id="SF")
    with open('test_data/lines_schema.json') as schema:
        validate(instance=transit_lines_live, schema=json.load(schema))
