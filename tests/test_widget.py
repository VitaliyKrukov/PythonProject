import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def test_mask_account_card():
    assert mask_account_card("Visa 1234567891234567") == "Visa 1234 56** **** 4567"


@pytest.mark.parametrize("number_cards_or_check, result", [("Visa 5987654657432156", "Visa 5987 65** **** 2156"),
                                                           ("Счет 45672312344509871237", "Счет **1237"),
                                                           (12.21, "Введите номер карты или номер счета"),
                                                           (123456789, "Введите номер карты или номер счета"),
                                                           ("Цифры", "Введите номер карты или номер счета"),])

def test_mask_account_card_mark (number_cards_or_check, result):
    assert mask_account_card(number_cards_or_check) == result



@pytest.fixture
def test_get_date():
    assert get_mask_account("2024-03-11T02:26:18.671407") == '("11.03.2024")'


@pytest.mark.parametrize("date, expected", [("2022-12-22T02:26:18.671407", '("22.12.2022")'),
                                            ("2017-03-10T02:26:18.671407", '("10.03.2017")'),
                                            (123456789, "Введите верный формат данных"),
                                            ("Цифры", "Введите верный формат данных"),
                                            (22.33, "Введите верный формат данных"),
                                            (True, "Введите верный формат данных"),
                                            ([1, 2, 3, 4], "Введите верный формат данных")])
def test_get_date_mark(date, expected):
    assert get_date(date) == expected
