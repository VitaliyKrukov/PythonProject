import pandas as pd


def processing_function_csv(file_path: str) -> list[dict]:
    """Функция, которая принимает путь файла csv
    и обрабатывает в список словарей"""
    try:
        reader = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    transact = reader.to_dict("records")
    return transact


def processing_function_excel(file_path: str) -> list[dict]:
    """Функция, которая принимает путь файла excel
    и обрабатывает в список словарей"""
    try:
        reader = pd.read_excel(file_path)
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    transact = reader.to_dict("records")
    return transact
