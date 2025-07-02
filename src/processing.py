from typing import Iterable
import json

"""Функция, возвращающая новый список словарей по заданному ключу"""


def filter_by_state(dictionarys_list: Iterable[list], state="EXECUTED") -> list:
    result = []
    """Перебор значений по ключу"""
    for dictionary in dictionarys_list:
        if dictionary.get('state') == state:
            result.append(dictionary)
    return result


"""Функция, возвращающая новый список словарей, отсортированных по дате"""


def sort_by_date(dictionarys_list: Iterable[list]) -> list:
    sorted_list = sorted(dictionarys_list, key=lambda dictionarys_list: dictionarys_list['date'], reverse=True)
    return sorted_list


if __name__ == '__main__':
    dictionarys_input = input()
    # Заменяем одинарные кавычки на двойные
    dictionarys_input = dictionarys_input.replace("'", '"')
    # Преобразуем в JSON
    dictionarys_list = json.loads(dictionarys_input)
    # Вызов функции
    filter_by_state(dictionarys_list)

    dictionarys_input = input()
    # Заменяем одинарные кавычки на двойные
    dictionarys_input = dictionarys_input.replace("'", '"')
    # Преобразуем в JSON
    dictionarys_list = json.loads(dictionarys_input)
    sort_by_date(dictionarys_list)
