from typing import Union


def filter_by_state(scroll: list[dict[str, Union[int, str]]], meaning: str = "EXECUTED") -> list[
    dict[str, Union[int, str]]]:
    count_dict = []
    for element in scroll:
        if element["state"] == meaning:
            count_dict.append(element)
    return count_dict


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "Rety",
    )
)


def sort_by_date(scroll: list[dict[str, Union[int, str]]], direction: bool = True) -> list[
    dict[str, Union[int, str]]]:
    sorted_list = sorted(scroll, key=lambda x: x['date'], reverse=direction)
    return sorted_list


