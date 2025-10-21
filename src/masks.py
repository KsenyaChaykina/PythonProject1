import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('C:\\Users\\Agilent_2022\\PycharmProjects\\PythonProject1\\logs\\masks.log', 'w',
                                   encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

"""Маска номер карты"""


def get_mask_card_number(card_num: str) -> str:
    len_card_num = len(card_num)
    if len_card_num > 6:
        try:
            logger.info("Получен номер карты с маской")
            mask = "******"
            result = ""
            count = 0
            """Создание номера карты с маской"""
            card_num_str = str(card_num[:6] + mask + card_num[12:])
            """Разделение номера карты для выведения по 4 символа через пробел"""
            for i in card_num_str:
                result += i
                count += 1
                if count % 4 == 0:
                    result += " "
            return result
        except Exception:
            logger.info("Произошла ошибка")
            return ''
    else:
        return ''


"""Маска номер счета"""


def get_mask_account(account_num: str) -> str:
    len_account_num = len(account_num)
    if len_account_num > 6:
        try:
            logger.info("Получен номер счета с маской")
            mask = "**"
            """Создание номера счета с маской"""
            result = str(mask + account_num[-4:])
            return result
        except Exception:
            logger.info("Произошла ошибка")
            return ''
    else:
        return ''


if __name__ == '__main__':
    account_num = input()
    print(get_mask_account(account_num))
    card_num = input()
    print(get_mask_card_number(card_num))
