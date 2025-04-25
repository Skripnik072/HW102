import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int) -> str:
    """Функция возвращает маску номера банковской карты"""
    logger.info(f'Введен номер банковской карты {number_card}')
    result = str(number_card)[0:4] + " " + str(number_card)[4:6] + "** " + "****" + " " + str(number_card)[-4:]
    logger.info(f'Выведена маска номера карты {result}')
    return result


print(get_mask_card_number(7000792289606361))


def get_mask_account(bank_account: int) -> str:
    """Функция возвращает маску банковского счёта"""
    logger.info(f'Введен номер счёта {bank_account}')
    resalt = "**" + str(bank_account)[-4:]
    logger.info(f'Выведена маска номера счёта {resalt}')
    return resalt


print(get_mask_account(73654108430135874305))
