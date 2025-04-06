import json


def function_accepts_json(file_name):
    """Функция обрабатывающая json файл"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                file_lis = json.load(file)
                if type(file_lis) is not list:
                    return []
                return file_lis
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
