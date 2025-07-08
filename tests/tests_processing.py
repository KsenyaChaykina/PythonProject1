from src.processing import filter_by_state
from src.processing import sort_by_date


def test_filter_by_state(dictionarys):
    for item in dictionarys:
        assert isinstance(item, dict)
        assert 'state' in item


def test_sort_by_date(dictionarys):
    for item in dictionarys:
        assert isinstance(item, dict)
        assert 'date' in item

# Преобразование строки в список словарей
#     try:
#     dictionaries_list = json.loads(dictionaries_input)
#     filter_by_state(dictionaries_list)
# except json.JSONDecodeError:
#     print("Ошибка: неверный формат JSON.")
