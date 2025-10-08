import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\logs\\utils.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

"""Возвращает список словарей с данными о финансовых транзакциях"""


def financial_transactions(file_path: str) -> list[dict]:
    try:
        logger.info("Получен список словарей с данными о финансовых транзакциях")
        with open(file_path, 'r', encoding='utf-8') as f:
            data_list = json.load(f)
            return data_list
        """Обработка ошибок"""
    except FileNotFoundError:
        logger.error('Произошла ошибка: Файл не найден')
        return []
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
        return []


if __name__ == '__main__':
    #Успешный вывод в консоль
    print(financial_transactions('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\data\\operations.json'))
    #Ошибка "Файл не найден"
    #print(financial_transactions('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\dataa\\operations.json'))

