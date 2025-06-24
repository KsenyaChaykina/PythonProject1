from typing import Iterable


dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(dict_list: Iterable[str], state='EXECUTED') -> None:
    result = []
    for dict in dict_list:
        if dict.get('state') == state:
            result.append(dict)
    print(result)


filter_by_state(dict_list)


dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def sort_by_date(dict_list: Iterable[str]) -> None:
    sorted_list = sorted(dict_list, key=lambda dict: dict['date'], reverse=True)
    print(sorted_list)


sort_by_date(dict_list)
