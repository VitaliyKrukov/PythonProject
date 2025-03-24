from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


def print6(xs):
    for i, x in enumerate(xs):
        print(x)
        if i == 5:
            break


def test_filter_by_currency(generator_transactions):
    filter_test = filter_by_currency(generator_transactions, "USD")
    assert next(filter_test) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_test) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_error():
    filter_test = filter_by_currency("hi", "USD")
    assert list(filter_test) == []


def test_filter_by_currency_rub(generator_transactions):
    filter_test = filter_by_currency(generator_transactions, "RUB")
    assert next(filter_test) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(filter_test) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_eur(generator_transactions):
    filter_test = filter_by_currency(generator_transactions, "EUR")
    assert list(filter_test) == []


def test_transaction_descriptions(generator_transactions):
    gen_transaction = transaction_descriptions(generator_transactions)
    assert next(gen_transaction) == "Перевод организации"
    assert next(gen_transaction) == "Перевод со счета на счет"
    assert next(gen_transaction) == "Перевод со счета на счет"
    assert next(gen_transaction) == "Перевод с карты на карту"
    assert next(gen_transaction) == "Перевод организации"


def test_transaction_descriptions_not(generator_transactions_not_description):
    gen_transaction = transaction_descriptions(
        generator_transactions_not_description
    )
    assert list(gen_transaction) == []


def test_transaction_descriptions_str(generator_transactions):
    gen_transaction = transaction_descriptions("Helloy world")
    assert list(gen_transaction) == []


def test_transaction_descriptions_int(generator_transactions):
    gen_transaction = transaction_descriptions(123456789)
    assert list(gen_transaction) == []


def test_card_number_generator():
    card_number_test = card_number_generator(1, 5)
    assert next(card_number_test) == "0000 0000 0000 0001"
    "0000 0000 0000 0002"
    "0000 0000 0000 0003"
    "0000 0000 0000 0004"
    "0000 0000 0000 0005"


def test_card_number_generator_str():
    card_number_test = card_number_generator("start", "stop")
    assert list(card_number_test) == []


def test_card_number_generator_revers():
    card_number_test = card_number_generator(5, 1)
    assert list(card_number_test) == []


def test_card_number_generator_max():
    card_number_test = card_number_generator(
        9999999999999998, 9999999999999999
    )
    assert next(card_number_test) == "9999 9999 9999 9998"
    "9999 9999 9999 9999"


def test_card_number_generator_bool():
    card_number_test = card_number_generator(True, False)
    assert list(card_number_test) == []
