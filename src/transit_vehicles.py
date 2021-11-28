from downloader import download
from datetime import datetime


class TransitVehicle:
    def __init__(self, data_dict):
        # Only store needed data
        self.recorded_time = datetime.strptime(data_dict['RecordedAtTime'][:-1], "%Y-%m-%dT%H:%M:%S")
        vehicle_journey = data_dict['MonitoredVehicleJourney']
        self.line_ref = vehicle_journey['LineRef']
        self.direction_ref = vehicle_journey['DirectionRef']
        self.published_line_name = vehicle_journey['PublishedLineName']
        self.origin_name = vehicle_journey['OriginName']
        self.destination_name = vehicle_journey['DestinationName']
        self.monitored = vehicle_journey['Monitored']
        self.vehicle_location = vehicle_journey['VehicleLocation']


class TransitVehicles:
    def __init__(self, api_key, operator_id):
        self.__api_key = api_key
        self.operator_id = operator_id
        self.vehicles = []
        response = download('VehicleMonitoring', api_key, agency=operator_id)
        if response is None:
            raise ConnectionError("Could not download data")
        vehicle_activity = response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity']
        for vehicle in vehicle_activity:
            self.vehicles.append(TransitVehicle(vehicle))
