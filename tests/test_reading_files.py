import unittest
from unittest.mock import patch, mock_open

import pandas as pd

from src.reading_files import reading_transactions_csv, reading_transactions_excel

""" Тест на успешное чтение файла csv """


class TestDataReader(unittest.TestCase):
    def test_reading_transactions_csv(self):
        mock_csv_data = (
            "id;state;date;amount;currency_name;currency_code;from;to;description\n"
            "3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту\n"
            "593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту\n"
        )
        m = mock_open(read_data=mock_csv_data)
        with patch('builtins.open', m):
            transactions = reading_transactions_csv('test_file.csv')
        m.assert_called_once_with('test_file.csv', 'r', newline='', encoding='utf-8')
        expected_transactions = [
            {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740',
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
             'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
            {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': '30368',
             'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
             'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'}
        ]
        """ Сравниваем результат с ожидаемым """
        self.assertEqual(transactions, expected_transactions)

    """ Тест ошибки файл csv не найден """

    def test_reading_transactions_csv_file_not_found(self):
        m = mock_open()
        m.side_effect = FileNotFoundError
        with patch('builtins.open', m):
            transactions = reading_transactions_csv('test_file.csv')
        self.assertEqual(transactions, [])


""" Тест на успешное чтение файла Excel """


@patch('src.reading_files.pd.read_excel')
def test_reading_transactions_excel(mock_read_excel):
    mock_data = {
        'id': [157454.0, 2177828.0],
        'state': ['EXECUTED', 'EXECUTED'],
        'date': ['2020-08-01T07:40:25Z', '2022-04-14T15:14:21Z'],
        'amount': [11438.0, 24853.0],
        'currency_name': ['Won', 'Yuan Renminbi'],
        'currency_code': ['KRW', 'CNY'],
        'from': ['Discover 1588407825007798', 'Счет 38577962752140632721'],
        'to': ['Mastercard 6632952863435990', 'Счет 47657753885349826314'],
        'description': ['Перевод с карты на карту', 'Перевод со счета на счет']
    }
    mock_df = pd.DataFrame(mock_data)
    mock_read_excel.return_value = mock_df
    file_path = 'test_file.xlsx'
    result = reading_transactions_excel(file_path)
    mock_read_excel.assert_called_with(file_path)
    expected_result = [
        {'amount': 11438.0,
         'currency_code': 'KRW',
         'currency_name': 'Won',
         'date': '2020-08-01T07:40:25Z',
         'description': 'Перевод с карты на карту',
         'from': 'Discover 1588407825007798',
         'id': 157454.0,
         'state': 'EXECUTED',
         'to': 'Mastercard 6632952863435990'},
        {'amount': 24853.0,
         'currency_code': 'CNY',
         'currency_name': 'Yuan Renminbi',
         'date': '2022-04-14T15:14:21Z',
         'description': 'Перевод со счета на счет',
         'from': 'Счет 38577962752140632721',
         'id': 2177828.0,
         'state': 'EXECUTED',
         'to': 'Счет 47657753885349826314'}
    ]
    assert result == expected_result


""" Тест ошибки файл excel не найден """


@patch('src.reading_files.pd.read_excel')
def test_reading_transactions_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError
    file_path = 'test_file.xlsx'
    result = reading_transactions_excel(file_path)
    assert result == []
