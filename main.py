import os

from src.file_processing import (
    processing_function_csv,
    processing_function_excel,
)
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.regulation import search_transactions
from src.utils import function_accepts_json
from src.widget import get_date, mask_account_card


def main() -> None:
    """Главная функция собирающая весь проект в едино."""
    print(
        """Привет! Добро пожаловать в программу
         работы с банковскими транзакциями.\n
Выберите необходимый пункт меню:
\t1. Получить информацию о транзакциях из JSON-файла
\t2. Получить информацию о транзакциях из CSV-файла
\t3. Получить информацию о транзакциях из XLSX-файла
    """
    )
    result = ""
    lst_transaction = []

    while True:
        result = input().strip()
        if result == "1":
            print("Для обработки выбран JSON-файл.")
            lst_temp = function_accepts_json(
                os.path.join(
                    os.path.dirname(__file__), "data", "operations.json"
                )
            )
            for temp in lst_temp:
                dct = {
                    "id": temp.get("id", 0),
                    "state": temp.get("state", ""),
                    "date": temp.get("date", ""),
                    "amount": temp.get("operationAmount", {}).get(
                        "amount", ""
                    ),
                    "currency_name": temp.get("operationAmount", {})
                    .get("currency", {})
                    .get("name", ""),
                    "currency_code": temp.get("operationAmount", {})
                    .get("currency", {})
                    .get("code", ""),
                    "description": temp.get("description", ""),
                    "from": temp.get("from", ""),
                    "to": temp.get("to", ""),
                }
                lst_transaction.append(dct)
            break
        elif result == "2":
            print("Для обработки выбран CSV-файл.")
            lst_transaction = processing_function_csv(
                os.path.join(
                    os.path.dirname(__file__), "data", "transactions.csv"
                )
            )
            break
        elif result == "3":
            print("Для обработки выбран XLSX-файл.")
            lst_transaction = processing_function_excel(
                os.path.join(
                    os.path.dirname(__file__),
                    "data",
                    "transactions_excel.xlsx",
                )
            )
            break
        else:
            print("Введены не верные данные, выберите вариант из списка")

    set_str = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        result = input().strip()
        if result.upper() in set_str:
            lst_transaction = filter_by_state(lst_transaction, result.upper())
            break
        else:
            print(f"Статус операции {result} недоступен.")

    print("Отсортировать операции по дате? Да/Нет")
    result = input().strip()
    if result.lower() == "да":
        print("Отсортировать по возрасанию? Да/Нет")
        result = input().strip()
        lst_transaction = sort_by_date(lst_transaction, result != "да")

    print("Выводить только рублевые тразакции? Да/Нет")
    result = input().strip()
    if result.lower() == "да":
        filter_test = filter_by_currency(lst_transaction, "RUB")
        lst_transaction = list(filter_test)

    print(
        "Отфильтровать список транзакций по определенному"
        " слову в описании? Да/Нет"
    )
    result = input().strip()
    if result.lower() == "да":
        lst_transaction = search_transactions(
            lst_transaction, input("Введите слово для поиска: ").strip()
        )
    if len(lst_transaction) == 0:
        print(
            "Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
    else:
        print("\nРаспечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(lst_transaction)}\n")

        for transaction in lst_transaction:
            date = get_date(transaction["date"])
            description = transaction["description"]
            to_mask = mask_account_card(transaction["to"])
            if transaction.get("from"):
                from_mask = mask_account_card(transaction["from"])
            else:
                from_mask = ""
            amount = transaction["amount"]
            curense = transaction["currency_name"]

            print(f"{date} {description}")
            print(f"{from_mask + ' -> ' if from_mask else ''}{to_mask}")
            print(f"Сумма: {amount} {curense}\n")


if __name__ == "__main__":
    main()
