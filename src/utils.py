import json
import os
import logging
from external_api import get_user_convert


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_finans_tranz(path: str) -> dict:
    ''' Возвращает из JSON список словарей с финансовыми транзакциями'''
    if not os.path.exists(path):
        logger.error("Не найден путь к файлу")
        raise FileNotFoundError("Файл не найден")
    if os.path.getsize(path) == 0:
        logger.error("Файл не содержит информацию")
        raise ValueError("Файл пустой")
    try:
        with open(path, encoding='utf-8') as finans_file:
            try:
                list_tr_actions = json.load(finans_file)
                logger.info(f'Файл {path} загружен из JSON')
            except json.JSONDecodeError:
                logger.error("Ошибка обработки кода")
                return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    logger.info('Файл преобразован в список словарей')
    return list_tr_actions


if __name__ == '__main__':
    list_j = get_finans_tranz("date\\oper1.json")
    print(list_j)


def get_t_action_currency(tr_action: dict, amount=None) -> float:
    '''Функция принимает тразакцию и возвращет её сумму'''
#    amount_rub = ""
    if tr_action == {}:
        logger.error("Нет информации в транзакции")
        raise TypeError("Транзакция пустая")
    for i in tr_action:
        if 'operationAmount' not in i:
            logger.error("Нет такого ключа в транзакции")
            raise KeyError("Ключ не найден")
        summ_amount = i["operationAmount"]["amount"]
        try:
            float(summ_amount)
        except ValueError:
            logger.error("Введена некорректная сумма")
            raise ValueError("Некорректная сумма")
        if float(summ_amount) <= 0.0:
            logger.error("Введена некорректная сумма")
            raise ValueError("Некорректная сумма")
        if i["operationAmount"]["currency"]["code"] == "RUB":
            logger.info('Транзакция выполнена в валюте RUB')
            amount_rub = float(i["operationAmount"]["amount"])
        elif i["operationAmount"]["currency"]["code"] == "USD" or "EUR":
            logger.info('Транзакция не в валюте RUB. Конвертируем с помощью API')
            amount = i["operationAmount"]["amount"]
            currency = i["operationAmount"]["currency"]["code"]
            amount_rub = get_user_convert(amount, currency)
        else:
            continue
    logger.info(f'Сумма транзакции: {amount_rub} руб.')
    return amount_rub


list_j = get_finans_tranz("date\\oper1.json")
amount_rub = get_t_action_currency(list_j)
print(f"Сумма транзакции {amount_rub} руб.")
