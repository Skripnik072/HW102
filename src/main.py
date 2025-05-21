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
while source not in ["1", "2", "3"]:
    print("Некорректный выбор. Выберите заново")
    source = input()
if source == "1":
    print("Для обработки выбран JSON-файл.")
    list_new = get_finans_tranz("date\\operations.json")
elif source == "2":
    print("Для обработки выбран CSV-файл.")
    list_new = get_external_csv("date\\transactions.csv")
elif source == "3":
    print("Для обработки выбран XLSX-файл.")
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
if sort_rus == "нет":
    list_trans = sorted_list
else:
    list_trans = filter_by_currency(sorted_list, currency="RUB")
# print(list_trans)

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filter_y = input()
filter_yes = filter_y.lower()
while filter_yes not in ["да", "нет"]:
    print("Некорректный выбор. Ввведите да или нет!")
    filter_y = input()
    filter_yes = filter_y.lower()
if filter_yes == "нет":
    list_transactions = list_trans
else:
    print("Введите слово для поиска")
    word = input()
    n = 0
for i in list_trans:
    if word in i['description']:
        n =+ 1
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

    date_trans = get_date(i['date'])
    from_trans = mask_account_card(i.get('from', "00000000000000000000"))
    to_trans = mask_account_card(i['to'])
    print(f"{date_trans} {i['description']}")
    print(f"{from_trans} -> {to_trans}")
    print(f"Сумма {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print("")
