from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[list[Any], Any, None]:
    """Функция из списка словарей выбирает транзакции по заданной валюте"""
    new_list = []
    if isinstance(transactions, list) is False:
        raise TypeError('Не верный тип данных')
    elif isinstance(currency, str) is False:
        raise TypeError('Не верный тип данных')
    elif transactions == []:
        raise ValueError("Список пустой")
    else:
        for dict in transactions:
            if dict["operationAmount"]["currency"]["name"] == currency:
                new_list.append(dict)
                yield new_list
                new_list = []

# result = filter_by_currency([], "USD")


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

# print(next(result))


def transaction_descriptions(transactions: list) -> Generator[Any, Any, None]:
    """Функуия возвращает описание транзакций из списка словарей"""
    new_string = ""
    if isinstance(transactions, list) is False:
        raise TypeError('Не верный тип данных')
    elif transactions == []:
        raise ValueError("Список пустой")
    else:
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

# result = transaction_descriptions([])
# print(next(result))


def card_number_generator(begin_number: int, end_number: int) -> list[str]:
    """Функция генерирует номера банковских карт"""
    int_card = 10000000000000000 + begin_number
    my_list = []
    if isinstance(begin_number, int) is False:
        raise TypeError('Не верный тип данных')
    elif isinstance(end_number, int) is False:
        raise TypeError('Не верный тип данных')
    elif not begin_number or not end_number:
        raise TypeError('Нет начала или конца диапазона')
    elif begin_number < 0 or end_number < 0:
        raise ValueError("Введено некорреткное число")
    else:
        for _ in range(begin_number, end_number):
            new_string = str(int_card)
            my_string = new_string[1:5] + " " + new_string[5:9] + " " + new_string[9:13] + " " + new_string[13:]
            my_list.append(my_string)
            int_card += 1
    return my_list


for card_number in card_number_generator(1, 3):
    print(card_number)
