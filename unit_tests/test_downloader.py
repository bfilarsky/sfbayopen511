from source.downloader import downloader


def testCreateEndpointNoArgs():
    test_api = 'test_api'
    test_api_key = '123'
    endpoint = downloader.createEndpoint(test_api, test_api_key)
    assert endpoint == 'http://api.511.org/transit/test_api?api_key=123'


def testCreateEndpointSingleArg():
    test_api = 'test_api'
    test_api_key = '123'
    endpoint = downloader.createEndpoint(test_api, test_api_key, test_key='arg')
    assert endpoint == 'http://api.511.org/transit/test_api?api_key=123&test_key=arg'


def testCreateEndpointTwoArgs():
    test_api = 'test_api'
    test_api_key = '123'
    endpoint = downloader.createEndpoint(test_api, test_api_key, test_key='arg', test_key2='arg2')
    assert endpoint == 'http://api.511.org/transit/test_api?api_key=123&test_key=arg&test_key2=arg2' \
        or endpoint == 'http://api.511.org/transit/test_api?api_key=123&test_key2=arg2&test_key=arg'


def testdownloadDataNominal(requests_mock):
    mock_endpoint = 'http://test_endpoint/test_api'
    requests_mock.get(mock_endpoint, json={'test_key': 'test_value'})
    data = downloader.downloadData(mock_endpoint)
    assert data == '{"test_key": "test_value"}'


def testdownloadDataError(requests_mock):
    mock_endpoint = 'http://test_endpoint/test_api'
    requests_mock.get(mock_endpoint, status_code=400)
    data = downloader.downloadData(mock_endpoint)
    assert data is None


def testDownJSON(requests_mock):
    api_key = '123'
    endpoint = downloader.createEndpoint('test_api', api_key)
    requests_mock.get(endpoint, json={'test_key': 'test_value'})
    data = downloader.download('test_api', api_key)
    assert data == {"test_key": "test_value"}
