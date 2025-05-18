from collections import Counter, defaultdict

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

kat_dict = {'Перевод организации': 0, 'Перевод с карты на карту': 0, 'Открытие вклада': 0}


def list_from_dict(my_list: list, kat_dict: dict) -> dict:
    '''Функция преобразует список словарей транзакций в словарь, где ключи - названия категорий
    транзакций, а значения - количество операций в данной категории'''
    new_list = []
    new_dict = {}
    my_dict = defaultdict(list)
    for i in my_list:
        new_list.append(i['description'])
    counted = Counter(new_list)
    count = counted.most_common(10)
    print(count)
    for j in count:
        my_dict[j[0]] = j[1]
    for key1 in kat_dict.keys():
        for key, value in my_dict.items():
            if key1 == key:
                new_dict[key] = value
    return new_dict


# if __name__ == '__main__':
#    n_dict = list_from_dict(my_list, kat_dict)
#    print(n_dict)