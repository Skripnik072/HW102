def get_mask_card_number(number_card: str) -> str:
    """Функция возвращает маску номера банковской карты"""
    if number_card == "":
        raise ValueError('Не введён номер карты')
    elif str(number_card).isdigit() == False:
        raise ValueError('Некорректный номер')
    elif int(number_card) <= 0:
        raise ValueError('Неверный номер карты')
    elif len(str(number_card)) != 16:
        raise ValueError('Неверный номер карты')
    else:
        return str(number_card)[0:4] + " " + str(number_card)[4:6] + "** " + "****" + " " + str(number_card)[-4:]


# print(get_mask_card_number(7000792289606361))


def get_mask_account(bank_account: int) -> str:
    """Функция возвращает маску банковского счёта"""
    if bank_account == "":
        raise ValueError('Не введён номер счёта')
    elif str(bank_account).isdigit() == False:
        raise ValueError('Некорректный номер')
    elif int(bank_account) <= 0:
        raise ValueError('Неверный номер счёта')
    elif len(str(bank_account)) != 20:
        raise ValueError('Неверный номер счётф')
    else:
        return "**" + str(bank_account)[-4:]


print(get_mask_account(73654108430135874305))
