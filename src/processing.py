from typing import Iterable


dictionarys_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

"""Функция, возвращающая новый список словарей по заданному ключу"""
def filter_by_state(dictionarys_list: Iterable[list], state='EXECUTED') -> list:
    result = []
    """Перебор значений по ключу"""
    for dictionary in dictionarys_list:
        if dictionary.get('state') == state:
            result.append(dictionary)
    return result


filter_by_state(dictionarys_list)


dictionarys_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

"""Функция, возвращающая новый список словарей, отсортированных по дате"""
def sort_by_date(dictionarys_list: Iterable[list]) -> list:
    sorted_list = sorted(dictionarys_list, key=lambda dictionarys_list: dictionarys_list['date'], reverse=True)
    return sorted_list


sort_by_date(dictionarys_list)
