import csv
import pandas as pd


def get_external_csv(path: str) -> list[dict]:
    '''Функция принимает файл CSV и возвращает список словарей'''
    my_dict = {}
    my_list = []
    try:
        with open(path, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                my_dict = {"id": row['id'], "state": row["state"], "date": row["date"],
                           "amount": row["amount"], "currency_name": row["currency_name"],
                           "currency_code": row["currency_code"], "from": row["from"], "to": row["to"],
                           "description": row["description"]}
                my_list.append(my_dict)
#            print(my_list)
        return my_list
    except FileNotFoundError:
        raise FileNotFoundError ("Файл не найден")



# if __name__ == '__main__':
#    list_new = get_external_csv("date\\transactions.csv")
#    print(list_new)
