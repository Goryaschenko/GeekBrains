# """
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# """
# from prettytable import PrettyTable
#
# x = PrettyTable()
#
# maze = []  # Список всех чисел
# maze_of_quotient = []  # Список с кол-вом кратных чисел
#
# for i in range(2, 100):  # Генератор списка всех чисел
#     maze.append(int(i))
#
# for s in range(2, 10):  # Генератор делителей
#     k = 0
#     for i, el in enumerate(maze):  # Проходим по списку чисел каждым делителем
#         f = el % s
#         if f == 0:
#             k += 1
#     maze_of_quotient.append(k)  # Добавлем в список кол-во кратных чисел
#
# x.field_names = ["2", "3", "4", "5", "6", "7", "8", "9"]  # Заголовок таблицы
# x.add_rows([maze_of_quotient])  # Вывод данных в таблицу относительно заголовка
# print("В последовательности от 2 до 9 .Количество чисел кратных:")
# print(x)  # Вывод таблицы при помощи prettytable

"""
2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
т.к. именно в этих позициях первого массива стоят четные числа.
"""
#
# import random
#
#
# def rand_maze(maze_range):
#     maze_of_numbers = []  # Сгенерированный массив
#     maze_of_index = []  # Массив индексов четных чисел
#
#     for i in range(maze_range):
#         maze_of_numbers.append(int(random.randint(0, 100)))
#
#     for i, el in enumerate(maze_of_numbers):
#         if el % 2 == 0:
#             maze_of_index.append(i+1)
#     print(f"Сгенерированный массив: {maze_of_numbers}")
#     print(f"Четные числа находятся на {maze_of_index} местах")
#
#
# rand_maze(int(input("Введи длину случайного массива")))

# """
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# """
# import random
#
#
# def trans_max_min(maze_range):
#     maze_of_numbers = []  # Сгенерированный массив
#     max_el = 0
#     min_el = 0
#     maze_of_max = []
#     maze_of_min = []
#     for i in range(maze_range):
#         maze_of_numbers.append(int(random.randint(0, 100)))
#     print(f"Сгенерированный массив: {maze_of_numbers}")
#
#     for i in maze_of_numbers:  # Ищем максимум
#         if i > max_el:
#             max_el = i
#
#     for i in maze_of_numbers:  # Ищем минимум
#         if i < max_el:
#             min_el = i
#             for i in maze_of_numbers:
#                 if i < min_el:
#                     min_el = i
#
#     for i, el in enumerate(maze_of_numbers):  # Находим все индексы максимумов
#         if el == max_el:
#             maze_of_max.append(i)
#             for i, el in enumerate(maze_of_numbers):  # Находим все индексы минимумов
#                 if el == min_el:
#                     maze_of_min.append(i)
#
#     for i, el in enumerate(maze_of_numbers):  # Ищем элементы в списке и меняем их на противоположные
#         if el == max_el:
#             maze_of_numbers[i] = min_el
#         elif el == min_el:
#             maze_of_numbers[i] = max_el
#
#     print(f"Максимум = {max_el}, Минимум = {min_el}")
#     print(f"Индексы максимумов {maze_of_max}, Индексы минимумов {maze_of_min}")
#     print(f"Новый массив: {maze_of_numbers}")
#
#
# trans_max_min(int(input("Введи длину случайного массива: ")))

"""
4. Определить, какое число в массиве встречается чаще всего.
"""
# import random
#
#
# def repeatability(maze_range):
#     maze_of_sum = {}
#     maze_of_numbers = [1, 2, 1, 3, 0, 3]  # Сгенерированный массив
#     for i in range(maze_range):
#         maze_of_numbers.append(int(random.randint(0, 100)))
#     print(f"Сгенерированный массив: {maze_of_numbers}")
#
#     for i in maze_of_numbers:
#         if i in maze_of_sum:
#             maze_of_sum[i] += 1
#         else:
#             maze_of_sum[i] = 1
#     print(maze_of_sum)
#
#
# repeatability(int(input("Введи длину случайного массива")))

"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
# import random
#
#
# def max_of_min(maze_range):
#     index = []
#     mm_element = 0
#     maze_of_numbers = []  # Сгенерированный массив
#     for i in range(maze_range):
#         maze_of_numbers.append(int(random.randint(-10, 10)))
#     print(f"Сгенерированный массив: {maze_of_numbers}")
#
#     for i in maze_of_numbers:
#         if i < mm_element:
#             mm_element = i
#
#     for i, el in enumerate(maze_of_numbers):
#         if el < 0:
#             if el > mm_element:
#                 mm_element = el
#                 index.append(i+1)
#     print(f"Максимальный отрицаьтельный элемент = {mm_element}, Находится на {index} месте списка")
#
#
# max_of_min(int(input("Введи длину случайного массива : ")))

"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random


def trans_max_min(maze_range):
    maze_of_numbers = []  # Сгенерированный массив
    max_el = 0
    min_el = 0

    for i in range(maze_range):
        maze_of_numbers.append(int(random.randint(0, 100)))
    print(f"Сгенерированный массив: {maze_of_numbers}")

    for i in maze_of_numbers:  # Ищем максимум
        if i > max_el:
            max_el = i

    for i in maze_of_numbers:  # Ищем минимум
        if i < max_el:
            min_el = i
            for i in maze_of_numbers:
                if i < min_el:
                    min_el = i
"""
7. В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
"""

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
