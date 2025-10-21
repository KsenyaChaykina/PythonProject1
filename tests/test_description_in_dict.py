import unittest
from collections import Counter

from src.description_in_dict import my_list_of_dictionaries, process_bank_search


class TestMyListDictionaries(unittest.TestCase):
    def test_my_list_of_dictionaries(self):
        # Исходный список словарей
        data = [
            {"date": "2023-10-04", "description": "Проезд на метро", "amount": 100},
            {"date": "2023-10-05", "description": "Оплата в супермаркете", "amount": 150},
            {"date": "2023-10-06", "description": "Перевод другу", "amount": 200}
        ]

        result_1 = [{'date': '2023-10-04', 'description': 'Проезд на метро', 'amount': 100}]
        result_error = []

        self.assertEqual(my_list_of_dictionaries(data, 'проезд'), result_1)  # успешное выполнение
        self.assertEqual(my_list_of_dictionaries(data, 'перелет'), result_error)  # ошибка


class TestProcessBankSearch(unittest.TestCase):
    def test_process_bank_search(self):
        data = [
            {"date": "2023-10-04", "description": "Проезд на метро", "amount": 100},
            {"date": "2023-10-05", "description": "Оплата в супермаркете", "amount": 150},
            {"date": "2023-10-06", "description": "Перевод другу", "amount": 200},
        ]

        key = "description"
        unique_categories = list(set(description[key] for description in data if key in description))

        result_1 = Counter({'Проезд на метро': 1, 'Оплата в супермаркете': 1, 'Перевод другу': 1})
        result_error = []

        self.assertEqual(process_bank_search(data, unique_categories), result_1)  # успешное выполнение
        self.assertEqual(process_bank_search(data, 'перелет'), result_error)  # ошибка
