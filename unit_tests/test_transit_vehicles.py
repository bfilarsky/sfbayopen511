from sfbayopen511.transit_vehicles import TransitVehicles

import json
from unittest.mock import patch
from datetime import datetime
import pytest


@patch('sfbayopen511.transit_vehicles.download')
def test_parse_server_error(mock_download):
    mock_download.return_value = None
    with pytest.raises(ConnectionError):
        TransitVehicles('123', 'SF')


@patch('sfbayopen511.transit_vehicles.download')
def test_parse_nominal(mock_download):
    with open('test_data/vehicles_nominal.json') as file:
        mock_download.return_value = json.load(file)
    transit_vehicles = TransitVehicles('123', 'SF')
    assert len(transit_vehicles.vehicles) == 3
    for idx, vehicle in enumerate(transit_vehicles.vehicles):
        assert vehicle.recorded_time == datetime.strptime(f'2021-11-28T2{idx}:00:00', "%Y-%m-%dT%H:%M:%S")
        assert vehicle.line_ref == f'{idx}'
        assert vehicle.direction_ref == 'OB'
        assert vehicle.published_line_name == f'Test Line {idx}'
        assert vehicle.origin_name == 'Test Origin'
        assert vehicle.destination_name == 'Test Destination'
        assert vehicle.monitored is True
        assert vehicle.vehicle_location == {"Longitude": "-122.402451",
                                            "Latitude": "37.7884674"}
