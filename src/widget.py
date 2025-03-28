import masks


def mask_account_card(my_string: str) -> str:
    """Функция обработки банковских карт или счетов"""
    new_string = ""
    my_list = my_string.split()
    if "Счет" in my_string:
        for my_item in my_list:
            if my_item.isdigit():
                new_item = masks.get_mask_account(int(my_item))
    else:
        for my_item in my_list:
            if my_item.isdigit():
                new_item = masks.get_mask_card_number(int(my_item))
    my_list[-1] = new_item
    new_string = " ".join(my_list)

    return new_string


# print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_string: str) -> str:
    """Функция преобразования даты"""
    # my_string = date_string[0:-16]
    # new_list = my_string.split("-")[::-1]
    # new_string = ".".join(new_list)
    return ".".join(date_string[0:-16].split("-")[::-1])


# print(get_date("2024-03-11T02:26:18.671407"))
