import os
from typing import Any

import requests
from dotenv import load_dotenv


def return_amount(transaction: dict[Any, Any]) -> float:
    """Функция отображающая курс валют"""
    curancy = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if curancy == "RUB":
        return float(amount)
    else:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={curancy}&amount={amount}"
        )
        headers = {"apikey": api_key}
        try:
            respons = requests.get(url, headers=headers)
        except requests.exceptions.RequestException:
            print("ошибка http запроса")
            return 0.0
        else:
            if respons.status_code != 200:
                print("ошибка кода")
                return 0.0
            info = respons.json()
            return float(info["result"])
