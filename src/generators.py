from typing import Iterable
import json

with open('../transactions.json', 'r', encoding='utf-8') as file:
    transactions = json.load(file)

"""Функция выдает транзакции, где валюта операции соответствует заданной"""


def filter_by_currency(transactions: Iterable[list], code) -> list:
    for transaction in transactions:
        if 'code' in transaction:
            if transaction["operationAmount"]["currency"]["code"] == code:
                yield transaction
            else:
                yield ''


"""Функция возвращает описание каждой операции по очереди"""


def transaction_descriptions(transactions: Iterable[list]) -> str:
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]
        else:
            yield ''


"""Генератор номеров банковских карт"""


def card_number_generator(start, end):
    for num in range(start, end + 1):
        yield '{:04d} {:04d} {:04d} {:04d}'.format(num // 10 ** 12, (num // 10 ** 8) % 10 ** 4,
                                                   (num // 10 ** 4) % 10 ** 4, num % 10 ** 4)


if __name__ == '__main__':
    for transaction in filter_by_currency(transactions, 'USD'):
        print(transaction)

    for transaction in transaction_descriptions(transactions):
        print(transaction)

    start = int(input())
    end = int(input())
    for num in card_number_generator(start, end):
        print(num)
