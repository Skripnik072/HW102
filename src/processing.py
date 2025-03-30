def filter_by_state(my_list: list, state: str = 'EXECUTED') -> list:
    '''Функция отфильтровывает список словарей по ключу
    :rtype: object
    '''
    new_list = []
#    for dict in my_list:
#        for key, value in dict.items():
#            if value == state:
#                new_list.append(dict)
#    return new_list
    if isinstance(my_list, list) is False:
        raise TypeError('Не верный тип данных')
    elif isinstance(state, str) is False:
        raise TypeError('Не верный тип данных')
    elif my_list == []:
        raise ValueError("Список пустой")
    elif state != 'EXECUTED' and state != 'CANCELED':
        raise KeyError("Некорректный ключ")
    else:
        return [i for i in my_list if i['state'] == state]




# print(filter_by_state([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}], 'CANCELED'))


def sort_by_date(my_list: list, reverse: bool = True) -> list:
    '''Функция сортирует список словарей по дате'''
    if isinstance(my_list, list) is False:
        raise TypeError('Не верный тип данных')
    elif my_list == []:
        raise ValueError("Список пустой")
    else:
        sorted_list = sorted(my_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2020-07-03T18:35:29.512364'},
                     {'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]))
