from src import masks


"""Обработка данных о картах и счетах"""


def mask_account_card(user_input: str) -> str:
    if 'Счет' in user_input:
        """Создание номера счета с маской"""
        account = user_input[-20:]
        return 'Счет ' + masks.get_mask_account(account)
    else:
        number_card = "".join(user_input[-16:].split())
        return user_input[:16] + masks.get_mask_account(number_card)


"""Обработка даты"""


def get_date(user_date: str) -> str:
    """Соединяем день, месяц и год в дату"""
    date = ".".join([user_date[8:10], user_date[5:7], user_date[:4]])
    return date


if __name__ == "__main__":
    user_input = input()
    mask_account_card(user_input)
    """Обработка даты"""
    user_date = input()
    get_date(user_date)
