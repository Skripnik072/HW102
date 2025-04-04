from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[list[Any], Any, None]:
    """Функция из списка словарей выбирает транзакции по заданной валюте"""
    new_list = []
    for dict in transactions:
        if dict["operationAmount"]["currency"]["name"] == currency:
            new_list.append(dict)
            yield new_list
            new_list = []


# result = [dict for dict in transactions if dict["operationAmount"]["currency"]["name"] == currency]

result = filter_by_currency(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ],
    "USD",
)

print(next(result))


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    """Функуия возвращает описание транзакций из списка словарей"""
    new_string = ""
    for dict in transactions:
        new_string = dict["description"]
        yield new_string


descrip = transaction_descriptions(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ],
)
for _ in range(2):
    print(next(descrip))


def card_number_generator(begin_number: int, end_number: int) -> list[str]:
    """Функция генерирует номера банковских карт"""
    int_card = 10000000000000000 +begin_number
    my_list = []
    for _ in range(begin_number, end_number):
        new_string = str(int_card)
        my_string = new_string[1:5] + " " + new_string[5:9] + " " + new_string[9:13] + " " + new_string[13:]
        my_list.append(my_string)
        int_card += 1
    return my_list


for card_number in card_number_generator(1, 5):
    print(card_number)
