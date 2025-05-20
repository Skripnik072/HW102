import re


my_list = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
           'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
           'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'},
          {'id': '3598919',
           'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso',
           'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
           'description': 'Перевод с карты на карту'},
          {'id': '593027', 'state': 'CANCELED', 'date':
           '2023-07-22T05:02:01Z', 'amount': '30368', 'currency_name': 'Shilling', 'currency_code': 'TZS',
           'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
          {'id': '366176', 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': '29482',
           'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
           'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
          {'id': '5380041', 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': '23789',
           'currency_name': 'Peso', 'currency_code': 'UYU', 'from': '', 'to': 'Счет 23294994494356835683',
           'description': 'Открытие вклада'},
          {'id': '1962667', 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': '18588',
           'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
           'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
          {'id': '5294458', 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': '16836',
           'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
           'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'}]


def select_from_dict(my_list: list, string: str) -> list:
    '''Функция отфильтровывает словарь по регулярному выражению (строке)'''
    new_list = []
    if not isinstance(string, str):
        raise TypeError('Некорректный тип транзакции')

    for i in my_list:
        if re.search(string, i["description"], flags=re.I):
            new_list.append(i)
        else:
            continue
    return new_list


# if __name__ == '__main__':
#    new_list = select_from_dict(my_list, "Перевод организации")
