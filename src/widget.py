from src.masks import get_mask_account, get_mask_card_number  # Импортируем необходимые функции.


def mask_account_card(finding_numbers: str) -> str:  # Пишем функцию, которая будет обрабатывать информацию.
    """Функцию, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if type(finding_numbers) == str:
        string_numbers = ""
        string_letters = ""
        for finding in finding_numbers:
            if finding.isdigit():
                string_numbers += finding
            else:
                string_letters += finding
        string_lower = string_letters.lower()  # Пишем условие, которое сортирует на разные функции.
        if "счет" in string_lower and len(string_numbers) == 20:
            return f"{string_letters}{get_mask_account(int(string_numbers))}"
        elif len(string_numbers) == 16:
            return f"{string_letters}{get_mask_card_number(int(string_numbers))}"
        elif string_numbers == "":
            return "Введите номер карты или номер счета"
        else:
            return "Введите номер карты или номер счета"
    else:
        return "Введите номер карты или номер счета"

print(mask_account_card("Visa 5987654657432156"))

def get_date(string_data: str) -> str:  # Пишем функцию, которая форматирует код в удобно читаемый вид.
    """Функция, которая принимает на вход строку с датой и создает удобный формат для чтения."""
    if type(string_data) == str and len(string_data) >= 10:
        return f'("{string_data[8:10]}.{string_data[5:7]}.{string_data[0:4]}")'
    else:
        return "Введите верный формат данных"
