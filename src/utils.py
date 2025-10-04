import json

"""Возвращает список словарей с данными о финансовых транзакциях"""


    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
            return data_list
        """Обработка ошибок"""
    except FileNotFoundError:
        return []
    except Exception as e:
        return []


if __name__ == '__main__':
    print(financial_transactions('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\operations.json'))
