from src.regulation import counting_operations, search_transactions

operateons = [
    {
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
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Оплата покупки",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
]


def test_search_transactions():
    assert search_transactions(operateons, "перевод") == [
        {
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
    ]


def test_search_transactions_emptiness():
    assert search_transactions([], "") == []


def test_counting_operations():
    assert counting_operations(operateons, ["перевод", "оплата"]) == {
        "перевод": 1,
        "оплата": 1,
    }


def test_counting_operations_emptiness():
    assert counting_operations([], []) == {}
