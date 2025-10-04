import os
from dotenv import load_dotenv
from src.utils import financial_transactions
import requests

"""Загрузка переменных их файла env"""
load_dotenv()

API_KEY = os.getenv('API_KEY')


def transaction_amount(transaction: dict) -> float:
    if transaction['operationAmount']['currency']['code'] == 'RUB':
        return float(transaction['operationAmount']['amount'])
    try:
        my_amount = transaction['operationAmount']['amount']
        my_from = transaction['operationAmount']['currency']['code']
        my_to = "RUB"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={my_to}&from={my_from}&amount={my_amount}"
        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url, headers=headers)

        return float(response.json()['result'])
        # Обработка ошибки ключа
    except KeyError:
        return 0


if __name__ == '__main__':
    transactions = financial_transactions('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\operations.json')
    for transaction in transactions:
        print(transaction_amount(transaction))