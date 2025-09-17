import os

from config import ROOT_DIR
from src.decorators import log

"""Маска номер карты"""

@log()
def get_mask_card_number(card_num: str) -> str:
    mask = "******"
    result = ""
    count = 0
    """Создание номера карты с маской"""
    if len(card_num) >= 12:
        card_num_str = str(card_num[:6] + mask + card_num[12:])
        """Разделение номера карты для выведения по 4 символа через пробел"""
        for i in card_num_str:
            result += i
            count += 1
            if count % 4 == 0:
                result += " "
        result = result.strip()
        return result
    else:
        return ''


"""Маска номер счета"""

@log()
def get_mask_account(account_num: str) -> str:
    if len(account_num) >= 3:
        mask = "**"
        """Создание номера счета с маской"""
        result = str(mask + account_num[-4:])
        return result
    else:
        return ''


if __name__ == '__main__':
    card_num = input()
    get_mask_card_number(card_num)
    account_num = input()
    get_mask_account(account_num)
