from transit_operators import TransitOperators

import json
from unittest.mock import patch
import pytest


@patch('transit_operators.download')
def test_parse_server_error(mock_download):
    mock_download.return_value = None
    with pytest.raises(ConnectionError):
        TransitOperators('123')


@patch('transit_operators.download')
def test_parse_nominal(mock_download):
    with open('test_data/operators_nominal.json') as file:
        mock_download.return_value = json.load(file)
    transit_operators = TransitOperators('123')
    assert len(transit_operators.operators) == 5
    for idx, operator in enumerate(transit_operators.operators):
        assert operator.name == "Test Transit Operator " + str(idx)
        assert operator.id == "T" + str(idx)
        assert operator.monitored == bool(idx % 2)


@patch('transit_operators.download')
def test_parse_fixed_monitored(mock_download):
    with open('test_data/operators_fixed_monitored.json') as file:
        mock_download.return_value = json.load(file)
    transit_operators = TransitOperators('123')
    assert len(transit_operators.operators) == 5
    for idx, operator in enumerate(transit_operators.operators):
        assert operator.name == "Test Transit Operator " + str(idx)
        assert operator.id == "T" + str(idx)
        assert operator.monitored == bool(idx % 2)
