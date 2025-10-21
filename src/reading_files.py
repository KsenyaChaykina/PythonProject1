import csv

import pandas as pd


def reading_transactions_csv(file_path: str) -> list:
    """ Считывает финансовые операции из CSV-файла, принимает путь к файлу CSV
     в качестве аргумента и возвращает список словарей с транзакциями """
    try:
        transactions_csv = []
        with open(file_path, 'r', newline='', encoding='utf-8') as csv_f:
            rd_transactions_csv = csv.DictReader(csv_f, delimiter=';')
            for row in rd_transactions_csv:
                transactions_csv.append(row)
        return transactions_csv
        """ Обработка ошибки отсутствия файла CSV """
    except FileNotFoundError:
        return []


def reading_transactions_excel(file_path: str) -> list:
    """ Считывает финансовые операции из EXCEL-файла, принимает путь к файлу Excel
     в качестве аргумента и возвращает список словарей с транзакциями """
    try:
        rd_transactions_excel = pd.read_excel(file_path)
        transactions_excel = rd_transactions_excel.to_dict(orient='records')
        return transactions_excel
        """ Обработка ошибки отсутствия файла EXCEL """
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    # print(reading_transactions_csv("C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\transactions.csv"))
    print(reading_transactions_excel("C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\transactions_excel.xlsx"))
