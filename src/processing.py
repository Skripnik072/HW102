def filter_by_state(my_list: list, state: str = 'EXECUTED') -> list:
    '''Функция отфильтровывает список словарей по ключу state'''
    new_list = []
    for dict in my_list:
        status_key = dict.get('state')
        for key, value in dict.items():
            if value == state:
                new_list.append(dict)
    return new_list

#    return [i for i in my_list if i['state'] == state]


# print(filter_by_state([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}], "EXECUTED"))


def sort_by_date(my_list: list, reverse: bool = True) -> list:
    '''Функция сортирует список словарей по дате'''
    sorted_list = sorted(my_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list


# print(sort_by_date([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]))

def filter_by_currency(my_list: list, currency: str = 'RUB') -> list:
    '''Функция отфильтровывает список словарей по ключу currency_code'''
    new_list = []

    return [i for i in my_list if i['operationAmount']['currency']['code'] == currency]


# my_list = [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount':
#           {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации',
#            'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
#           {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount':
#           {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации',
#            'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]

# print(filter_by_currency(my_list, currency="RUB"))

def filter_by_description(my_list: list, word: str) -> list:
    '''Функция отфильтровывает список словарей по слову из описания'''
    new_list = []

    return [i for i in my_list if word in i['description']]