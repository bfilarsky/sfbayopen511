from sfbayopen511.downloader import download


class TransitOperator:
    def __init__(self, data_dict):
        # Only store needed data
        self.name = data_dict['Name']
        self.id = data_dict['Id']
        # As of the creation of this file, the API incorrectly returns the key
        # as "Montiored"(sic)
        if 'Montiored' in data_dict:
            self.monitored = data_dict['Montiored']
        if 'Monitored' in data_dict:
            self.monitored = data_dict['Monitored']


class TransitOperators:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.operators = []
        response = download('operators', api_key)
        if response is None:
            raise ConnectionError("Could not download data")
        for transit_operator in response:
            self.operators.append(TransitOperator(transit_operator))
