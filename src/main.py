from src.utils

"""Сводный модуль для работы с транзакциями"""

print('''Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
      "Выберите необходимый пункт меню:
      
      1. Получить информацию о транзакциях из JSON-файла"
      2. Получить информацию о транзакциях из CSV-файла
      3. Получить информацию о транзакциях из XLSX-файла''')

source = input()
while source not in ["1", "2", "3"]:
    print("Некорректный выбор. Выберите заново")
    source = input()
if source == "1":
    print("Для обработки выбран JSON-файл.")
elif source == "2":
    print("Для обработки выбран CSV-файл.")
elif source == "3":
    print("Для обработки выбран XLSX-файл.")

print("Введите статус, по которому необходимо выполнить фильтрацию.")
print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
st_text = input()
status = st_text.lower()
while status not in ["executed", "canceled", "pending"]:
    print(f"Статус операции {status} недоступен.")
    print('''Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
    st_text = input()
    status = st_text.lower()
if status == "executed" or "canceled" or "pending":
    print(f"Операции отфильтрованы по статусу {status}")

print("Отсортировать операции по дате? Да/Нет")
sort_yes = input()
sort_tr = sort_yes.lower()
while sort_tr not in ["да", "нет"]:
    print("Некорректный ваыбор. Ввведите Да или Нет!")
    sort_yes = input()
    sort_tr = sort_yes.lower()
if sort_tr == "да":
    pass
else:
    pass

print("Отсортировать по возрастанию или по убыванию?")
sort_r = input()
sort_revers = sort_r.lower()
while sort_revers not in ["по возрастанию", "по убыванию"]:
    print("Некорректный ввод. Наберите по возрастанию или по убыванию.")
    sort_r = input()
    sort_revers = sort_r.lower()
if sort_revers == "по возрастанию":
    pass
else:
    pass

print("Выводить только рублевые транзакции? Да/Нет")
sort_rub = input()
sort_rus = sort_rub.lower()
while sort_rus not in ["да", "нет"]:
    print("Некорректный ваыбор. Ввведите Да или Нет!")
    sort_rub = input()
    sort_rus = sort_rub.lower()
if sort_rus == "да":
    pass
else:
    pass

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
word_d = input()
word_descripcion = word_d.lower()
while word_descripcion not in ["да", "нет"]:
    print("Некорректный ваыбор. Ввведите Да или Нет!")
    word_d = input()
    word_descripcion = word_d.lower()
if word_descripcion == "да":
    pass
else:
    pass

print("Распечатываю итоговый список транзакций...")

'''Выполнение основной программы'''


# Не найдено ни одной транзакции, подходящей под ваши условия фильтрации
