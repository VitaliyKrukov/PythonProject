import json
import logging
import os

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(os.path.join(
    os.path.dirname(__file__), "..\\logs\\", "utils.log"
),mode='w', encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(module)s.%(funcName)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def function_accepts_json(file_name: str) -> list:
    """Функция обрабатывающая json файл"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                file_lis = json.load(file)
                if type(file_lis) is not list:
                    logger.critical(f"Проверка {file_lis} на список")
                    return []
                logger.info(f"Вернул обработанный {file_name} в формате python")
                return file_lis
            except json.JSONDecodeError as e:
                logger.error(f"{e}")
                return []
    except FileNotFoundError as e:
        logger.error(f"{e}")
        return []
