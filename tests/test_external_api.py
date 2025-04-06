from unittest.mock import patch

import requests

from src.external_api import return_amount


def test_return_amount():
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert return_amount(data) == float(data["operationAmount"]["amount"])


@patch("requests.get")
def test_return_amount_exept(test_mock_get, capsys):
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    test_mock_get.side_effect = requests.exceptions.RequestException
    assert return_amount(data) == 0.0
    captured = capsys.readouterr()
    assert captured.out == "ошибка http запроса\n"


@patch("requests.get")
def test_return_amount_status_code(test_mock_get, capsys):
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    test_mock_get.return_value.status_code = 100
    assert return_amount(data) == 0.0
    captured = capsys.readouterr()
    assert captured.out == "ошибка кода\n"


@patch("requests.get")
def test_return_amount_status_amount_result(test_mock_get):
    data = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    test_mock_get.return_value.status_code = 200
    test_mock_get.return_value.json.return_value = {"result": 104.12}
    assert return_amount(data) == 104.12
