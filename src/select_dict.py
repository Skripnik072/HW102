import re


def select_from_dict(my_dict: dict, string: str) -> dict:
    '''Функция отфильтроввывает словарь по регулярному выражению (сроке)'''
    for i in my_dict:
        result = re.findall(r'\w+', i[description], flags=re.I)


if __name__ == '__main__':
    new_dict = select_from_dict(my_dict, "вклада")
