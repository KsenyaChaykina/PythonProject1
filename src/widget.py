from src import masks

"""Обработка данных о картах и счетах"""


def mask_account_card(user_input: str) -> str:
    card_type = ""
    replace_user_input = user_input.replace(" ", "")
    if not replace_user_input.isdigit() and not replace_user_input.isalpha():
        if 'Счет' in user_input:
            """Создание номера счета с маской"""
            account = user_input[-20:]
            return 'Счет ' + masks.get_mask_account(account)
        else:
            for i in user_input:
                if i.isalpha() or i.isspace():
                    card_type += i
            number_card = "".join(user_input[-16:].split())
            return card_type + masks.get_mask_card_number(number_card)
    else:
        return 'Ошибка ввода данных'


"""Обработка даты"""


def get_date(user_date: str) -> str:
    """Соединяем день, месяц и год в дату"""
    times = user_date[:user_date.find("T")].split("-")
    reversed_times = times[::-1]
    if len(times) < 2:
        return 'Ошибка ввода данных'
    else:
        return ".".join(reversed_times)


#if __name__ == "__main__":
    #user_input = input()
    #mask_account_card(user_input)
    """Обработка даты"""
    #user_date = input()
    #get_date(user_date)
