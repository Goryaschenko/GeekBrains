"""Задача - 1 Поиск максимума из трех чисел"""

a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

m = a
if m < b:
    m = b
if m < c:
    m = c

print(f"Max number = {m}")


## Вариант без хранения переменной ##
if a > b:
    if a > c:
        print(f"Max a = {a}")
    else:
        print(f"Max c = {c}")
else:
    if b > c:
        print(f"Max b = {b}")
    else:
        print(f"Max c = {c}")

######################################
######################################

'''
Задача - 2 Вычислить значение функции y=f(x)
Дана функция y=f(x):
y = 2x - 10, если x > 0 
y = 0, если x = 0 
y = 2 * |x| - 1, если x < 0
Требуется найти значение функции по введенному значению Х.
Алгоритм решения задачи сводится к следующим шагам:
Шаг 1. Пользователь вводит значение Х.
Шаг 2. Если Х  > 0, вычислить y = 2*x-10.
Шаг 2.1. Если Х = 0, то  y = 0.
Шаг 2.2. y = 2*|x|-1.
Шаг 3. Выводим значение y на экран
'''

x = input("Введи значение числа Х: ")
if x[0] == "-" and x[1:].isdigit() or x.isdigit():
    x = int(x)
else:
    x = 0

if x > 0:
    y = 2 * x - 10
elif x == 0:
    y = 0
else:
    y = 2 * abs(x) - 1

print(f"Значение функции: {y = }")

"""
Задание - 3
Алгоритм решения задачи в словесном представлении:
Шаг 1. Если первое число делится на второе без остатка, вывести сообщение об этом.
Шаг 2. Иначе вывести сообщение о том, что первое число не делится на второе нацело, затем найти остаток от деления и вывести его.
Шаг 3. В конце программы найти частное от деления чисел и вывести его.
 """
## Первый вариант

a = int(input('a = '))
b = int(input('b = '))

if a % b == 0:
    print(f"{a} делится на {b}")
else:
    print(f"{a} не делится на {b}")
    print(f"Остаток: {a % b}")
print(f"Частное: {a // b}")

## 2-й Вариант

if (res := a % b):
    print(f"{a} не делится на {b}")
    print(f"Остаток: {res}")
else:
    print(f"{a} делится на {b}")

'''
Задача 4
Принять число с клавиатуры и перевести его в байты или килобайты  —  по выбору пользователя.
Определим изначально, что для перевода числа в байты пользователь вводит ‘b’, а в килобайты  —  ‘k’. 
 
Алгоритм решения:
Шаг 1. Пользователь вводит значение.
Шаг 2. Пользователь выбирает единицы измерения.
Шаг 3. Если выбран перевод в байты, умножить число на 1024.
Шаг 4. Если выбран перевод в килобайты, разделить число на 1024.
 
'''

n = int(input("Число: "))
change_type = input("Перевести в байты (b) или килобайты (k): ")
if change_type.lower() == 'b':
    print(f"{n} Кб = {n * 1024} байт")
elif change_type.lower() == 'k':
    print(f"{n} байт = {n / 1024} Кб")