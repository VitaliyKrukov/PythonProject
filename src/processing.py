from typing import Union  # Импортируем Union


def filter_by_state(
    scroll: list[dict[str, Union[int, str]]], meaning: str = "EXECUTED"
) -> Union[list[dict[str, Union[int, str]]], str]:  # Создаем функцию, которая отсортирует список
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    if type(scroll) is list:
        count_dict = []
        for element in scroll:
            if element.get("state", "") == meaning:
                count_dict.append(element)
        return count_dict
    else:
        return "Введите верные данные"


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(
    scroll: list[dict[str, Union[int, str]]], direction: bool = True
) -> list[dict[str, Union[int, str]]]:  # Создаем функцию, которая сортирует по дате
    """Функция возвращает новый список, отсортированный по дате (date)"""
    sorted_list = sorted(scroll, key=lambda x: str(x.get("date", "")), reverse=direction)
    return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
