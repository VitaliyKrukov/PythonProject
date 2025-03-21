import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    assert (
        mask_account_card("Visa 1234567891234567")
        == "Visa 1234 56** **** 4567"
    )


@pytest.mark.parametrize(
    "number_cards_or_check, result",
    [
        ("Счет 45672312344509871237", "Счет **1237"),
        (12.21, "Введите номер карты или номер счета"),
        (True, "Введите номер карты или номер счета"),
        (123456789, "Введите номер карты или номер счета"),
        ("Цифры", "Введите номер карты или номер счета"),
        ("", "Введите номер карты или номер счета"),
    ],
)
def test_mask_account_card_mark(number_cards_or_check, result):
    assert mask_account_card(number_cards_or_check) == result


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == '("11.03.2024")'


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2017-13-10T02:26:18.671407", "Введите верный формат данных"),
        (123456789, "Введите верный формат данных"),
        ("Цифры", "Введите верный формат данных"),
        (22.33, "Введите верный формат данных"),
        (True, "Введите верный формат данных"),
        ([1, 2, 3, 4], "Введите верный формат данных"),
        ("", "Введите верный формат данных"),
    ],
)
def test_get_date_mark(date, expected):
    assert get_date(date) == expected
