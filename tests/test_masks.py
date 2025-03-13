import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def test_get_mask_card_number():
    assert get_mask_card_number(1234567891234567) == "1234 56** **** 4567"


@pytest.mark.parametrize("card_number, expected", [(5987654657432156, "5987 65** **** 2156"),
                                                   (4567234509871237, "4567 23** **** 1237"),
                                                   (123456783648389834507, "Введите 16 цифр номера карты"),
                                                   (123456789, "Введите 16 цифр номера карты"),
                                                   ("Цифры", "Введите 16 цифр номера карты"),
                                                   (22.33, "Введите 16 цифр номера карты"),
                                                   (True, "Введите 16 цифр номера карты"),
                                                   ([1, 2, 3, 4,], "Введите 16 цифр номера карты")])
def test_get_mask_card_number_mark(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.fixture
def test_get_mask_account():
    assert get_mask_account(12345674829891234567) == "**4567"


@pytest.mark.parametrize("card_account, expected", [(59876546574321564893, "**4893"),
                                                    (45672345098712371583, "**1583"),
                                                    (123456783648389834507324, "Введите 20 цифр номера счета"),
                                                    (123456789, "Введите 20 цифр номера счета"),
                                                    ("Цифры", "Введите 20 цифр номера счета"),
                                                    (22.33, "Введите 20 цифр номера счета"),
                                                    (True, "Введите 20 цифр номера счета"),
                                                    ([1, 2, 3, 4], "Введите 20 цифр номера счета")])
def test_get_mask_card_number_mark(card_account, expected):
    assert get_mask_account(card_account) == expected
