import pytest
import requests
import requests_mock

from app import check_url

def test_check_url_up():
    with requests_mock.Mocker() as m:
        m.get("https://example.com", status_code=200)
        assert check_url("https://example.com") == "UP"

def test_check_url_down_status():
    with requests_mock.Mocker() as m:
        m.get("https://example.com", status_code=500)
        assert check_url("https://example.com") == "DOWN"

def test_check_url_down_exception():
    with requests_mock.Mocker() as m:
        m.get("https://example.com", exc=requests.exceptions.ConnectTimeout)
        assert check_url("https://example.com") == "DOWN"
