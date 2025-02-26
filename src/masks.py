def get_mask_card_number(number_card: int) -> str:
    """Функцию маскировки номера банковской карты которая принимает номер карты и маскирует 6 цыфр в середине номера"""
    text_number = str(number_card)  # праброзуем строку в текст
    mask_numbers = "** ****"  # пишем переменную для маскировски цыфр
    resul = f"{text_number[0:4]} {text_number[5:7]}{mask_numbers} {text_number[-5:-1]}"
    return resul


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета которая принимает счет и возвращает последние 4 цыфры и маскирует 2 перд ними"""
    text_number2 = str(account_number)  # преабразуем строку в текст
    mask_numbers2 = "**"  # пишем переменную для маскировки цыфр
    resul = f"{mask_numbers2}{text_number2[-5:-1]}"
    return resul
