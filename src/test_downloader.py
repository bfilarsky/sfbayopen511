#!/bin/python
import downloader

def test_downloader():
    data = downloader.download_data("operators")
    assert data.status_code == 200
