from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(generator_transactions_shorts):
    filter_test = filter_by_currency(generator_transactions_shorts, "RUB")
    assert next(filter_test) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "amount": "67314.70",
        "currency_name": "руб.",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_error():
    filter_test = filter_by_currency("hi", "USD")
    assert list(filter_test) == []


def test_filter_by_currency_eur(generator_transactions_shorts):
    filter_test = filter_by_currency(generator_transactions_shorts, "EUR")
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
