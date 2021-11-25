from downloader import download


class TransitOperator:
    def __init__(self, data_dict):
        # Explicitly store commonly used variables, others can be left to the data dict
        self.name = data_dict['Name']
        self.id = data_dict['Id']
        # As of the creation of this file, the API incorrectly returns the key
        # as "Montiored"(sic)
        if 'Montiored' in data_dict:
            self.monitored = data_dict['Montiored']
        if 'Monitored' in data_dict:
            self.monitored = data_dict['Monitored']
        self.data_dict = data_dict


class TransitOperators:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.operators = []
        operators_text_list = download('operators', api_key)
        print(operators_text_list)
        for transit_operator in operators_text_list:
            self.operators.append(TransitOperator(transit_operator))
