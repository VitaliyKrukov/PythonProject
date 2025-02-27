from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(finding_numbers: str) -> str:
    """Функцию, которая умеет обрабатывать информацию как о картах, так и о счетах, а так же маскирует информацию за счет другой функции."""
    string_numbers = ""
    string_letters = ""
    for finding in finding_numbers:
        if finding.isdigit():
            string_numbers += finding
        else:
            string_letters += finding

    string_lower = string_letters.lower()
    numbers_int = int(string_numbers)
    if "счет" not in string_lower:
        result = get_mask_card_number(numbers_int)

    else:
        result = get_mask_account(numbers_int)

    return f"{string_letters}{result}"


print(mask_account_card('Счет 64686473678894779589'))


def get_date(string_data: str) -> str:
    """Функция, которая принимает на вход строку с датой и создает удобный формат для чтения."""
    return f"(\"{string_data[8:10]}.{string_data[5:7]}.{string_data[0:4]}\") "
