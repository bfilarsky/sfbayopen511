from downloader import download


class TransitLine:
    def __init__(self, data_dict):
        # Only store needed data
        self.name = data_dict['Name']
        self.id = data_dict['Id']
        self.transport_mode = data_dict['TransportMode']
        self.monitored = data_dict['Monitored']


class TransitLines:
    def __init__(self, api_key, operator_id):
        self.__api_key = api_key
        self.lines = []
        response = download('lines', api_key, operator_id=operator_id)
        if response is None:
            raise ConnectionError("Could not download data")
        for transit_line in response:
            self.lines.append(TransitLine(transit_line))
