from utils import get_finans_tranz
from external_csv import get_external_csv
from external_xls import get_external_xls
from processing import filter_by_state, sort_by_date, filter_by_currency, filter_by_description
from widget import get_date, mask_account_card


"""Сводный модуль для работы с транзакциями"""

print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
      "Выберите необходимый пункт меню:
      
      1. Получить информацию о транзакциях из JSON-файла"
      2. Получить информацию о транзакциях из CSV-файла
      3. Получить информацию о транзакциях из XLSX-файла''')

source = input()
list_new = []
choice_file = "0"
while source not in ["1", "2", "3"]:
    print("Некорректный выбор. Выберите заново")
    source = input()
if source == "1":
    print("Для обработки выбран JSON-файл.")
    choice_file = "1"
    list_new = get_finans_tranz("date\\operations.json")
elif source == "2":
    print("Для обработки выбран CSV-файл.")
    choice_file = "2"
    list_new = get_external_csv("date\\transactions.csv")
elif source == "3":
    print("Для обработки выбран XLSX-файл.")
    choice_file = "3"
    list_new = get_external_xls("date\\transactions_excel.xlsx")

print("Введите статус, по которому необходимо выполнить фильтрацию.")
print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
list_state = []
stat_in = input()
status = stat_in.upper()
while status not in ["EXECUTED", "CANCELED", "PENDING"]:
    print(f"Статус операции {status} недоступен.")
    print('''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    stat_in = input()
    status = stat_in.upper()
if status in ["EXECUTED", "CANCELED", "PENDING"]:
    print(f"Операции отфильтрованы по статусу {status}")
    list_state = filter_by_state(list_new, status)
# print(list_state)
print(choice_file)

print("Отсортировать операции по дате? Да/Нет")
sort_yes = input()
sort_tr = sort_yes.lower()
while sort_tr not in ["да", "нет"]:
    print("Некорректный выбор. Ввведите Да или Нет!")
    sort_yes = input()
    sort_tr = sort_yes.lower()
if sort_tr == "нет":
    sorted_list = list_state
else:
    print("Отсортировать по возрастанию или по убыванию?")
    sort_r = input()
    sort_revers = sort_r.lower()
    while sort_revers not in ["по возрастанию", "по убыванию"]:
        print("Некорректный ввод. Наберите по возрастанию или по убыванию.")
        sort_r = input()
        sort_revers = sort_r.lower()
    if sort_revers == "по возрастанию":
        sorted_list = sort_by_date(list_state, reverse=False)
    else:
        sorted_list = sort_by_date(list_state, reverse=True)

print("Выводить только рублевые транзакции? Да/Нет")
sort_rub = input()
sort_rus = sort_rub.lower()
while sort_rus not in ["да", "нет"]:
    print("Некорректный выбор. Ввведите Да или Нет!")
    sort_rub = input()
    sort_rus = sort_rub.lower()
if sort_rus == "да" and choice_file == "1":
    list_trans = filter_by_currency(sorted_list, currency="RUB")
elif sort_rub == "да" and choice_file == "2" or "3":
    list_trans = [i for i in sorted_list if i.get('currency_code') == "RUB"]
else:
    list_trans = sorted_list

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filter_y = input()
filter_yes = filter_y.lower()
word = ""
while filter_yes not in ["да", "нет"]:
    print("Некорректный выбор. Ввведите да или нет!")
    filter_y = input()
    filter_yes = filter_y.lower()
if filter_yes == "нет":
    list_transactions = list_trans
elif filter_yes == "да":
    print("Введите слово для поиска")
    word = input()
    n = 0
    for i in list_trans:
        if word in i['description']:
            n += 1
    while n == 0:
        print("Нет таких слов в описании транзакций. Введите другое слово")
        word = input()
    list_transactions = filter_by_description(list_trans, word)

length_list = len(list_transactions)
if length_list == 0:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
print("Распечатываю итоговый список транзакций...")

print(f"Всего банковских операций в выборке: {length_list}")
for i in list_transactions:
    if choice_file in ["3", "2"]:
        amount_trans = i.get('amount')
        curreny_trans = i['currency_code']
        date_trans = ".".join(i['date'][0:-10].split("-")[::-1])
    else:
        amount_trans = i.get('operationAmount', {}).get('amount')
        curreny_trans = i.get('operationAmount', {}).get('currency', {}).get('name')
        date_trans = get_date(i['date'])

    descr_trans = i['description']
    to_trans = mask_account_card(i['to'])

    if i['description'] in "Открытие вклада":
        print(f"{date_trans} {descr_trans}")
        print(to_trans)
        print(f"Сумма {amount_trans} {curreny_trans}")
        print("")
    else:
        from_trans = mask_account_card(i.get('from'))
        print(f"{date_trans} {descr_trans}")
        print(f"{from_trans} -> {to_trans}")
        print(f"Сумма {amount_trans} {curreny_trans}")
        print("")
