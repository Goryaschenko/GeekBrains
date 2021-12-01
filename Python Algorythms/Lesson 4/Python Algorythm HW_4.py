"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import time
import random
from collections import Counter


def benchmark(func):
    def wrapper(*args):
        start = time.time()
        return_value = func(*args)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value
    return wrapper


def rand_maze(maze_range):
    maze_of_numbers = []  # Сгенерированный массив
    for i in range(maze_range):
        maze_of_numbers.append(int(random.randint(0, 100)))
    return maze_of_numbers

@benchmark
def repeatability(maze_of_numbers):
    maze_of_sum = {}
    for i in maze_of_numbers:
        if i in maze_of_sum:
            maze_of_sum[i] += 1
        else:
            maze_of_sum[i] = 1
    return maze_of_sum

@benchmark
def repeatability_count(maze_range):
    dict_of_sum = []
    for i in maze_range:
        dict_of_sum = Counter(maze_range).most_common(i)
    return dict_of_sum


# maze = rand_maze(int(input("Введи длину случайного массива: ")))  # 10000
# print(repeatability(maze))  # [*] Время выполнения: 0.0009975433349609375 секунд.
# print(repeatability_count(maze))  # [*] Время выполнения: 3.367030143737793 секунд.

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""
from math import sqrt
import cProfile
import re


def natural(n):
    maze = []
    for nom in range(2, n + 1):
        for mnom in maze:
            if mnom > sqrt(nom) + 1:
                maze.append(nom)
                break
            elif nom % mnom == 0:
                break
        else:
            maze.append(nom)
    return maze


def eratosthen(n):
    maze = list(range(2, n + 1))
    for i in maze:
        for elem in maze:
            if elem % i == 0 and elem != i:
                maze.remove(elem)
    return maze


numbers = int(input("Введи количество чисел"))
print(natural(numbers))
print(eratosthen(numbers))

cProfile.run('natural(numbers)')
cProfile.run('eratosthen(numbers)')


   #      765411 function calls in 0.331 seconds
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.331    0.331 <string>:1(<module>)
   #      1    0.235    0.235    0.331    0.331 Python Algorythm HW_4.py:63(natural)
   #      1    0.000    0.000    0.331    0.331 {built-in method builtins.exec}
   # 755815    0.096    0.000    0.096    0.000 {built-in method math.sqrt}
   #   9592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #
   #
   #       90411 function calls in 24.776 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000   24.776   24.776 <string>:1(<module>)
   #      1    6.243    6.243   24.776   24.776 Python Algorythm HW_4.py:77(eratosthen)
   #      1    0.000    0.000   24.776   24.776 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #  90407   18.533    0.000   18.533    0.000 {method 'remove' of 'list' objects}

