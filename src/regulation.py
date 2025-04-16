import re


def search_transactions(list_transactions: list[dict], search_bar: str) -> list[dict]:

    if not list_transactions or not search_bar:
        return []

    pattern = re.compile(search_bar, re.IGNORECASE)
    list_result = []

    for transactions in list_transactions:
        description = transactions.get('description')
        if description and pattern.search(description):
            list_result.append(transactions)
    return list_result

lst_card = ["оплата", "перевод"]
res = {"оплата": 0, "перевод": 2}
operateons = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]

def counting_operations(list_transactions: list[dict], categores: list)->dict:
    result = {}
    for cat in categores:
        lst = search_transactions(list_transactions, cat)
        counter = len(lst)
        result[cat] = counter
    return result



