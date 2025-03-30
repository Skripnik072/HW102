from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(my_string: str) -> str:
    """Функция обработки банковских карт или счетов"""
    global new_item
    new_string = ""
    if isinstance(my_string, str) is False:
        raise TypeError('Не верный тип данных')
    elif str(my_string) == "":
        raise ValueError("Не введён номер карты или счёта")
    elif 40 < len(str(my_string)) < 16:
        raise ValueError("Неверный номер карты")
    else:
        my_list = my_string.split()
        if "Счет" in my_string:
            for my_item in my_list:
                if my_item.isdigit():
                    new_item = get_mask_account(my_item)
        else:
            for my_item in my_list:
                if my_item.isdigit():
                    new_item = get_mask_card_number(my_item)
    my_list[-1] = new_item
    new_string = " ".join(my_list)

    return new_string


print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """Функция преобразования даты"""
    # my_string = date_string[0:-16]
    # new_list = my_string.split("-")[::-1]
    # new_string = ".".join(new_list)
    if isinstance(date_string, str) is False:
        raise TypeError('Не верный тип данных')
    elif str(date_string) == "":
        raise ValueError("Не введена строка с датой")
    elif date_string.isalpha():
        raise ValueError("В строке отсутствует дата")
    else:
        return ".".join(date_string[0:-16].split("-")[::-1])


print(get_date("2024-03-11T02:26:18.671407"))
