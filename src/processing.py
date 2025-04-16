def filter_by_state(
    scroll: list[dict], meaning: str = "EXECUTED"
) -> list[dict]:  # Создаем функцию, которая отсортирует список
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    if type(scroll) is list:
        count_dict = []
        for element in scroll:
            if element.get("state", "") == meaning:
                count_dict.append(element)
        return count_dict
    else:
        return []


def sort_by_date(
    scroll: list[dict], direction: bool = True
) -> list[dict]:  # Создаем функцию, которая сортирует по дате
    """Функция возвращает новый список, отсортированный по дате (date)"""
    sorted_list = sorted(
        scroll, key=lambda x: str(x.get("date", "")), reverse=direction
    )
    return sorted_list
