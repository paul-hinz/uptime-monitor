from app import check_url
from unittest.mock import patch, Mock

@patch("app.requests.get")
def test_check_url_up(mock_get):
    mock_response = Mock()
    mock_response.ok = True
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = check_url("https://example.com")
    assert result["status"] == "UP"
    assert result["code"] == 200

@patch("app.requests.get")
def test_check_url_down(mock_get):
    mock_get.side_effect = Exception("Connection failed")

    result = check_url("https://fail.com")
    assert result["status"] == "DOWN"
    assert result["code"] == "N/A"