def get_mask_card_number(number_card: int) -> str:
    """Функция возвращает маску номера банковской карты"""
    return str(number_card)[0:4] + " " + str(number_card)[4:6] + "** " + "****" + " " + str(number_card)[-4:]


# print(get_mask_card_number(7000792289606361))


def get_mask_account(bank_account: int) -> str:
    """Функция возвращает маску банковского счёта"""
    return "**" + str(bank_account)[-4:]


# print(get_mask_account(73654108430135874305))
