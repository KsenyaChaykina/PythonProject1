import re
from collections import Counter

transactions = [
    {"date": "2023-10-01", "description": "Оплата в супермаркете", "amount": 1500},
    {"date": "2023-10-02", "description": "Перевод другу", "amount": 2000},
    {"date": "2023-10-03", "description": "Оплата ЖКХ", "amount": 2500},
    {"date": "2023-10-04", "description": "Проезд на метро", "amount": 100},
    {"date": "2023-10-05", "description": "Оплата в супермаркете", "amount": 150},
    {"date": "2023-10-06", "description": "Перевод другу", "amount": 200},
    {"date": "2023-10-07", "description": "Оплата ЖКХ", "amount": 250},
    {"date": "2023-10-08", "description": "Проезд на такси", "amount": 1000}
]

""" Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
 возвращает список словарей с требуемой операцией """


def my_list_of_dictionaries(data_list: list[dict], my_description: str) -> list[dict]:
    my_dictionaries = []
    try:
        for transaction in data_list:
            if re.search(my_description, transaction["description"], flags=re.IGNORECASE):
                my_dictionaries.append(transaction)
        return my_dictionaries
    except Exception:
        return []


""" Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
 возвращает словарь, где ключи — названия категорий, значения — количество операций в каждой категории """

# Получение списка уникальных значений ключа description
key = "description"
unique_categories = list(set(description[key] for description in transactions if key in description))


def process_bank_search(data_list: list[dict], categories: list) -> list[dict]:
    result = Counter()
    try:
        for transaction in data_list:
            for value in transaction.values():
                if value in categories:
                    result[value] += 1
        return result
    except Exception:
        return []


if __name__ == '__main__':
    my_description = input()
    print(my_list_of_dictionaries(transactions, my_description))

    print(process_bank_search(transactions, unique_categories))
