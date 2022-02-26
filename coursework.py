# Курсовая работа студента группы 21-ЗИЭ Малюкова М.П. Вариант - 6
# Дисциплина - Программирование
# Задание: Получить список сотрудников со стажем выше введённого
# Отсортировать список по возростанию года вручения премии
# Файл с данными - data.json
# Исходный код - coursework.py
# Ссылка на Git - https://github.com/KULLEP/python-coursework-2021/
import os
import io
import json
clear = lambda: os.system('cls')


def inputNumber(str): # Проверка на ввод числа
    try:
        return int(input(str))
    except:
        return inputNumber('Введите цифру: ')


def dataLoad(): # Загрузка и обработка JSON файла
    f = io.open("data.json", mode="r", encoding="utf-8")
    return json.load(f)


def dataSort(arr, exp): # Выборка из массива на получение записей со стажем больше введённого и сортировка в порядке возрастания стажа
    arr = list(filter(lambda e: e['experience'] > exp, arr))
    return sorted(arr, key=lambda arr: arr['experience'])


def main(): # Главная функция
    clear()
    experience = inputNumber('Введите стаж: ')
    data = dataLoad()
    data = dataSort(data, experience)
    table_lines = '______________________________________________________________________________________\n'
    table_title = '|{:^5}|{:^15}|{:^30}|{:^15}|{:^15}|\n'.format('№', 'Фамилия','Название отдела', 'Год рождения', 'Стаж работы')
    table_data = ''
    index = 0
    for e in data:
        index += 1
        table_data += '|{:^5}|{:^15}|{:^30}|{:^15}|{:^15}|\n'.format(str(index), str(e['last_name']), str(e['department']), str(e['year_of_birth']), str(e['experience']))
    res_output = table_lines + table_title + table_lines + table_data + table_lines
    print(res_output)



main()
