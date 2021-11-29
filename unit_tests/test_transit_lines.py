from sfbayopen511.transit_lines import TransitLines

import json
from unittest.mock import patch
import pytest


@patch('sfbayopen511.transit_lines.download')
def test_parse_server_error(mock_download):
    mock_download.return_value = None
    with pytest.raises(ConnectionError):
        TransitLines('123', 'SF')


@patch('sfbayopen511.transit_lines.download')
def test_parse_nominal(mock_download):
    with open('test_data/lines_nominal.json') as file:
        mock_download.return_value = json.load(file)
    transit_lines = TransitLines('123', 'SF')
    assert len(transit_lines.lines) == 5
    for idx, operator in enumerate(transit_lines.lines):
        assert operator.name == "Line " + str(idx)
        assert operator.id == str(idx)
        if idx % 2 == 1:
            assert operator.monitored is True
            assert operator.transport_mode == "metro"
        else:
            assert operator.monitored is False
            assert operator.transport_mode == "bus"
