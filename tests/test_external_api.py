from unittest.mock import patch
import requests

from src.external_api import transaction_amount


def test_transaction_amount_rub():
    assert transaction_amount(
            {
                "operationAmount": {
                    "amount": "1",
                    "currency": {
                        "name": "USD",
                        "code": "RUB"
                    }
                }
            }
        ) == 1

@patch('requests.get', side_effect=KeyError('er'))
def test_transaction_error_key(mock_get):
    assert transaction_amount(
            {
                "operationAmount": {
                    "amount": "1",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                }
            }
        ) == 0

@patch('requests.get')
def test_transaction_amount_usd(mock_get):
    mock_get.return_value.json.return_value = {'result': 1}
    assert transaction_amount(
            {
                "operationAmount": {
                    "amount": "1",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                }
            }
        ) == 1
