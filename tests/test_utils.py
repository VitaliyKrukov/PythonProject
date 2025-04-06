import json
import os

from src.utils import function_accepts_json


def test_function_accepts_json(file_name):
    data = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file)
    assert function_accepts_json(file_name) == data
    os.remove(file_name)


def test_function_accepts_json_type(file_name):
    data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file)
    assert function_accepts_json(file_name) == []
    os.remove(file_name)


def test_function_accepts_json_open(file_name):
    assert function_accepts_json("") == []



def test_function_accepts_json_error(file_name):
    data = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(data))
    assert function_accepts_json(file_name) == []
    os.remove(file_name)
