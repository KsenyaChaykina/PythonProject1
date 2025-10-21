import unittest

from src.processing import filter_by_state, sort_by_date_ascending, sort_by_date_descending


class TestFilterByState(unittest.TestCase):
    def test_filter_by_state(self):
        data = [
            {"date": "2023-10-04", 'state': 'EXECUTED', "description": "Проезд на метро", "amount": 100},
            {"date": "2023-10-05", 'state': 'EXECUTED', "description": "Оплата в супермаркете", "amount": 150},
            {"date": "2023-10-06", 'state': 'CANCELED', "description": "Перевод другу", "amount": 200}
        ]
        result_1 = [{'amount': 100,
                     'date': '2023-10-04',
                     'description': 'Проезд на метро',
                     'state': 'EXECUTED'},
                    {'amount': 150,
                     'date': '2023-10-05',
                     'description': 'Оплата в супермаркете',
                     'state': 'EXECUTED'}]
        result_2 = []

        self.assertEqual(filter_by_state(data, 'EXECUTED'), result_1)  # успешное выполнение
        self.assertEqual(filter_by_state(data, 'sum'), result_2)

    def test_sort_by_date(self):
        data = [
            {"date": "2023-10-04", 'state': 'EXECUTED', "description": "Проезд на метро", "amount": 100},
            {"date": "2023-11-05", 'state': 'EXECUTED', "description": "Оплата в супермаркете", "amount": 150},
            {"date": "2023-10-06", 'state': 'CANCELED', "description": "Перевод другу", "amount": 200}
        ]

        result_1 = [{'amount': 100,'date': '2023-10-04','description': 'Проезд на метро','state': 'EXECUTED'},
                    {'amount': 200,'date': '2023-10-06','description': 'Перевод другу','state': 'CANCELED'},
                    {'amount': 150,'date': '2023-11-05','description': 'Оплата в супермаркете','state': 'EXECUTED'}]
        result_2 = [{'amount': 150, 'date': '2023-11-05', 'description': 'Оплата в супермаркете', 'state': 'EXECUTED'},
                    {'amount': 200, 'date': '2023-10-06', 'description': 'Перевод другу', 'state': 'CANCELED'},
                    {'amount': 100, 'date': '2023-10-04', 'description': 'Проезд на метро', 'state': 'EXECUTED'}]

        self.assertEqual(sort_by_date_ascending(data), result_1)  # по возрастанию
        self.assertEqual(sort_by_date_descending(data), result_2)  # по убыванию
