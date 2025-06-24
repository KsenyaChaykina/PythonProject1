from typing import Iterable
import json


dictionaries_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(dictionaries_list: Iterable[str], state='EXECUTED') -> None:
    result = []
    for dictionari in dictionaries_list:
        if dictionari.get('state') == state:
            result.append(dictionari)
    print(result)


filter_by_state(dictionaries_list)


dictionaries_list=[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def sort_by_date(dictionaries_list: Iterable[str]) -> None:
    sorted_dictionaries_list = sorted(dictionaries_list, key=lambda dictionari: dictionari['date'], reverse=True)
    print(sorted_dictionaries_list)


sort_by_date(dictionaries_list)