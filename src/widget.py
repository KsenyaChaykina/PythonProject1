"""Обработка данных о картах и счетах"""
user_input = input()


def mask_account_card(user_input: str) -> str:
    if user_input.find('Счет') != -1:
        mask = "**"
        """Создание номера счета с маской"""
        result = "Счет " + str(mask + user_input[-4:])
        return result
    else:
        mask = "******"
        result = ""
        count = 0
        card_type = ""
        """Оставляет только тип карты, без номера карты"""
        for i in user_input:
            if i.isalpha() or i.isspace():
                card_type += i
        """Оставляет только номер карты, без типа карты"""
        curd_num = ''.join(filter(str.isdigit, user_input))
        """Создание номера карты с маской"""
        card_num_str = str(curd_num[:6] + mask + curd_num[12:])
        """Разделение номера карты для выведения по 4 символа через пробел"""
        for i in card_num_str:
            result += i
            count += 1
            if count % 4 == 0:
                result += " "
        return f"{card_type}" + result


mask_account_card(user_input)


"""Обработка даты"""
user_input = input()


def get_date(user_input: str) -> str:
    """Вычисляем значения день, месяц, год"""
    day = user_input[8:10]
    month = user_input[5:7]
    year = user_input[:4]
    """Соединяем день, месяц и год в дату"""
    date = ".".join([day, month, year])
    return date


get_date(user_input)
