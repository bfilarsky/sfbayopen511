from jsonschema import validate
import json
from dotenv import load_dotenv
import os

from sfbayopen511.downloader import download


def test_nominal_schema():
    with open('test_data/operators_schema.json') as schema, open('test_data/operators_nominal.json') as nominal:
        validate(instance=json.load(nominal), schema=json.load(schema))


def test_fixed_schema():
    with open('test_data/operators_schema.json') as schema, open('test_data/operators_fixed_monitored.json') as nominal:
        validate(instance=json.load(nominal), schema=json.load(schema))


def test_live_schema():
    load_dotenv()
    api_key = os.environ.get("api_key")
    transit_operators_live = download('operators', api_key)
    with open('test_data/operators_schema.json') as schema:
        validate(instance=transit_operators_live, schema=json.load(schema))
