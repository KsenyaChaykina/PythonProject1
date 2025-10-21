import json

with open('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\transactions.json', 'r',
          encoding='utf-8') as file:
    my_transactions = json.load(file)

"""Функция выдает транзакции, где валюта операции соответствует заданной"""


def filter_by_currency(transactions: dict, code) -> list:
    filtered_transactions = []
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == code:
                """Если ключ найден, выводит транзакцию"""
                filtered_transactions.append(transaction)
        except KeyError:
            if transaction['currency_code'] == code:
                filtered_transactions.append(transaction)
    return filtered_transactions


"""Функция возвращает описание каждой операции по очереди"""


def transaction_descriptions(transactions: dict) -> str:
    for transaction in transactions:
        """Условие, проверяющее наличие ключа в словаре"""
        if "description" in transaction:
            """Если ключ найден, выводит назначение транзикции"""
            yield transaction["description"]
        else:
            yield ''


"""Генератор номеров банковских карт"""


def card_number_generator(start, end):
    for num in range(start, end + 1):
        """Разбивает 16-значное число на четыре группы по четыре цифры, каждую из которых разделяет пробел"""
        yield '{:04d} {:04d} {:04d} {:04d}'.format(num // 10 ** 12, (num // 10 ** 8) % 10 ** 4,
                                                   (num // 10 ** 4) % 10 ** 4, num % 10 ** 4)


if __name__ == '__main__':
    print(filter_by_currency(my_transactions, 'RUB'))

    for transaction in transaction_descriptions(my_transactions):
        print(transaction)

    start = int(input())
    end = int(input())
    for num in card_number_generator(start, end):
        print(num)
