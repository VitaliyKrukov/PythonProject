def get_mask_card_number(number_card: int) -> str:
    """Функцию маскировки номера банковской карты которая принимает номер карты и маскирует 6 цифр в середине номера"""
    if type(number_card) == int and len(str(number_card)) == 16:
        text_number = str(number_card)  # преобразуем строку в текст
        mask_numbers = "** ****"  # пишем переменную для маскировки цифр
        return f"{text_number[0:4]} {text_number[4:6]}{mask_numbers} {text_number[-4:]}"
    else:
        return "Введите 16 цифр номера карты"


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета которая принимает счет и возвращает последние 4 цифры
    и маскирует 2 передними"""
    if type(account_number) == int and len(str(account_number)) == 20:
        text_number_account = str(account_number)  # преобразуем строку в текст
        mask_numbers_account = "**"  # пишем переменную для маскировки цифр
        return f"{mask_numbers_account}{text_number_account[-4:]}"
    else:
        return "Введите 20 цифр номера счета"
