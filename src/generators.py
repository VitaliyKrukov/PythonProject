from typing import Generator, Union


def filter_by_currency(
    transactions: list[dict[str, Union[int, str]]], denomination: str
) -> Generator[dict[str, Union[int, str]], None, None]:
    """Функция которая сортирует список соварей
    на наличие определенного элемента (code)."""
    if (
        type(transactions) is list and type(denomination) is str
    ):  # пишем условие ввода данных
        list_code = [
            x
            for x in transactions
            if x["currency_code"] == denomination
        ]  # пишем логику кода
        for element in list_code:
            yield element


def transaction_descriptions(
    transaction: list[dict[str, Union[int, str]]],
) -> Generator[str | int, None, None]:
    if type(transaction) is list:  # пишем условие ввода данных
        """Функция которая сортирует список соварей
        на наличие определенного ключа (description)."""
        gen_iter = (
            x for x in transaction if "description" in x.keys()
        )  # пишем логику кода
        for element in gen_iter:
            yield element["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция которая генерирует номер
    карты в определенном диапозоне."""
    if type(start) is int and type(end) is int and start < end:
        # Перебираем все числа в диапазоне от start до end
        for number in range(start, end + 1):
            # Преобразуем число в строку и дополняем нулями до 16 цифр
            card_number = f"{number:016d}"
            # Форматируем номер карты в виде XXXX XXXX XXXX XXXX
            formatted_card_number = (
                f"{card_number[:4]} "
                f"{card_number[4:8]} "
                f"{card_number[8:12]} "
                f"{card_number[12:16]}"
            )
            yield formatted_card_number
