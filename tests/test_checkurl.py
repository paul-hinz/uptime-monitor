from requests import RequestException

import app
from unittest.mock import patch, Mock

@patch("app.requests.get")
def test_check_url_up(mock_get):
    mock_response = Mock()
    mock_response.ok = True
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = app.check_url("https://example.com")
    assert result["status"] == "UP"
    assert result["code"] == 200

@patch("app.requests.get")
def test_check_url_down(mock_get):
    mock_get.side_effect = RequestException("Connection failed")

    result = app.check_url("https://fail.com")
    assert result["status"] == "DOWN"
    assert result["code"] == "N/A"