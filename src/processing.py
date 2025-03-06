from typing import Union # Импортируем Union


def filter_by_state(scroll: list[dict[str, Union[int, str]]], meaning: str = "EXECUTED") -> list[
    dict[str, Union[int, str]]]: # Создаем функцию, которая отсортирует список
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
 соответствует указанному значению."""
    count_dict = []
    for element in scroll:
        if element["state"] == meaning:
            count_dict.append(element)
    return count_dict



def sort_by_date(scroll: list[dict[str, Union[int, str]]], direction: bool = True) -> list[
    dict[str, Union[int, str]]]: # Создаем функцию, которая сортирует по дате
    """Функция возвращает новый список, отсортированный по дате (date) """
    sorted_list = sorted(scroll, key=lambda x: x['date'], reverse=direction)
    return sorted_list


