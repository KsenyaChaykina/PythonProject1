from typing import Iterable

dictionaries_list=input()

def filter_by_state(dictionaries_list: Iterable[str], state='EXECUTED') -> None:
    result = []
    for dictionari in dictionaries_list:
        if dictionari.get('state') == state:
            result.append(dictionari)
    return(result)


filter_by_state(dictionaries_list)