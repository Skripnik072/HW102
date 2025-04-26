import pandas as pd
import openpyxl


def get_external_xls(path: str) -> list[dict]:
    '''Функция принимает файл Excel и возвращает список словарей'''
    my_dict = {}
    my_list = []
    try:
        excel_data = pd.read_excel(path)
        for index, row in excel_data.iterrows():
            my_dict = {"id": row['id'], "state": row["state"], "date": row["date"],
                       "amount": row["amount"], "currency_name": row["currency_name"],
                       "currency_code": row["currency_code"], "from": row["from"], "to": row["to"],
                       "description": row["description"]}
            my_list.append(my_dict)
        return my_list
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")


if __name__ == '__main__':
    list_new = get_external_xls("date\\transactions_excel.xlsx")
    print(list_new)

