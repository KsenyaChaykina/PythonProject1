from src.reading_files import reading_transactions_excel, reading_transactions_csv
from src.utils import financial_transactions
from src.processing import filter_by_state, sort_by_date_descending, sort_by_date_ascending
from src.generators import filter_by_currency
from src.description_in_dict import my_list_of_dictionaries
from src.widget import get_date, mask_account_card

""" Функция основной логики проекта, связка функционала"""


def main():
    """ Приветствие """
    print(
        'Привет! Добро пожаловать в программу работы с банковскими транзакциями.'
        ' \nВведите цифру, соответствующую пункту меню:\n '
        '1. Получить информацию о транзакциях из JSON-файла \n '
        '2. Получить информацию о транзакциях из CSV-файла \n '
        '3. Получить информацию о транзакциях из XLSX-файла')

    """ Выбор файла для обработки """

    while True:
        user_choice_1 = input()
        if user_choice_1 == '1':
            print('Для обработки выбран JSON-файл')
            transactions_data = financial_transactions(r'data\operations.json')
            break
        if user_choice_1 == '2':
            print('Для обработки выбран CSV-файл')
            transactions_data = reading_transactions_csv(r'data\transactions.csv')
            break
        if user_choice_1 == '3':
            print('Для обработки выбран XLSX-файл')
            transactions_data = reading_transactions_excel(r'data\transactions_excel.xlsx')
            break
        else:
            print('Не верный формат файла, попробуйте снова')

    """ Выбор статуса для обработки """

    while True:
        print(
            'Введите статус, по которому необходимо выполнить фильтрацию.'
            '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        user_choice_2 = input()
        upper_user_choice_2 = user_choice_2.upper()
        if upper_user_choice_2 in ["EXECUTED", "CANCELED", "PENDING"]:
            filtred_transactions_data = filter_by_state(transactions_data, upper_user_choice_2)
            print(f'Операции отфильтрованы по статусу {upper_user_choice_2}')
            break
        else:
            print(f'Статус операции {upper_user_choice_2} недоступен.')

    """Выбор пользователя для обработки операций:"""

    print('Уточните выборку операций. \nОтветьте пожалуйста на следующие вопросы:')
    while True:
        print('Отсортировать операции по дате? Да/Нет')
        user_choice_3 = input()
        lower_user_choice_3 = user_choice_3.lower()
        if lower_user_choice_3 != 'да' and lower_user_choice_3 != 'нет':
            print('Введите корректный ответ')
        else:
            if lower_user_choice_3 == 'нет':
                sort_by_date_transactions = filtred_transactions_data
                break
            if lower_user_choice_3 == 'да':
                while True:
                    print('Отсортировать по возрастанию или по убыванию?')
                    user_choice_4 = input()
                    lower_user_choice_4 = user_choice_4.lower()
                    if lower_user_choice_4 != 'по возрастанию' and lower_user_choice_4 != 'по убыванию':
                        print('Введите корректный ответ')
                    else:
                        if lower_user_choice_4 == 'по возрастанию':
                            sort_by_date_transactions = sort_by_date_ascending(filtred_transactions_data)
                            break
                        elif lower_user_choice_4 == 'по убыванию':
                            sort_by_date_transactions = sort_by_date_descending(filtred_transactions_data)
                            break
                break

    while True:
        print('Выводить только рублевые транзакции? Да/Нет')
        user_choice_5 = input()
        lower_user_choice_5 = user_choice_5.lower()
        if lower_user_choice_5 != 'да' and lower_user_choice_5 != 'нет':
            print('Введите корректный ответ')
        else:
            if lower_user_choice_5 == 'да':
                sort_by_currency_transactions = filter_by_currency(sort_by_date_transactions, 'RUB')
                break
            if lower_user_choice_5 == 'нет':
                sort_by_currency_transactions = sort_by_date_transactions
                break

    while True:
        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        user_choice_6 = input()
        lower_user_choice_6 = user_choice_6.lower()
        if lower_user_choice_6 != 'да' and lower_user_choice_6 != 'нет':
            print('Введите корректный ответ')
        elif lower_user_choice_6 == 'нет':
            filtered_by_word_transactions = sort_by_currency_transactions
            break
        else:
            if lower_user_choice_6 == 'да':
                print('Введите слово для фильтра списка:')
                user_choice_7 = input()
                title_user_choice_7 = user_choice_7.title()
                filtered_by_word_transactions = my_list_of_dictionaries(sort_by_currency_transactions,
                                                                        user_choice_7.title())
                break

    """Вывод результата"""

    print('Распечатываю итоговый список транзакций...')
    result_count = sum(isinstance(item, dict) for item in filtered_by_word_transactions)
    if result_count > 0:
        print(f'Всего банковских операций в выборке: {result_count}')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильрации')

    for transaction in filtered_by_word_transactions:
        try:
            transaction_date = transaction['date']
            transaction_description = transaction['description']
            transaction_num_from = transaction['from']
            transaction_num_to = transaction['to']
            try:
                transaction_sum = transaction['operationAmount']['amount']
                transaction_name = transaction['operationAmount']['currency']['name']
            except KeyError:
                transaction_sum = transaction['amount']
                transaction_name = transaction['currency_code']
            print(get_date(transaction_date), transaction_description)
            print(f'{mask_account_card(transaction_num_from)} -> {mask_account_card(transaction_num_to)}')
            print(f'Сумма: {transaction_sum} {transaction_name}')
        except KeyError:
            print(get_date(transaction_date), transaction_description)
            print(mask_account_card(transaction_num_to))
            print(f'Сумма: {transaction_sum} {transaction_name}')


if __name__ == "__main__":
    print(main())
