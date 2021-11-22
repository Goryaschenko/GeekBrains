'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

maze = list(str(input()))

if maze[0] == '-':
    maze.remove('-')
    n = '-' + maze[0]
    maze[0] = n
maze = [int(i) for i in maze]

prod_of_number = 1
for i in maze:
    prod_of_number *= i
sum_of_number = sum(maze)

print(f' Сумма введенных чисел = {sum_of_number}')
print(f' Произведение введенных чисел = {prod_of_number}')

"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
Объяснить полученный результат.
"""

bite_and = 5 & 6
bite_or = 5 | 6
bite_xor = 5 ^ 6
bite_a_not = ~5
bite_b_not = ~6

x = 5
bite_rshift = x << 2
bite_lshift = x >> 2

print(
      f' 5        6 \n'
      f'{bin(5)} {bin(6)}\n\n'

      f'Побитовое И: Если есть обе 1 = 1\n'
      f'{bin(5)} = 5\n &\n{bin(6)} = 6\n{bin(bite_and)} = {bite_and}\n\n',

      f'Побитовое ИЛИ: Если есть 1 = 1\n'
      f'{bin(5)} = 5\n |\n{bin(6)} = 6\n{bin(bite_or)} = {bite_or}\n\n'

      f'Побитовое исключающее ИЛИ: Инвертирует бит для которого маска = 1\n'
      f'{bin(5)} = 5\n ^\n{bin(6)} = 6\n{bin(bite_xor)} = {bite_xor}\n\n'

      f'Побитовое НЕ: меняет 1 на 0 и 0 на 1\n'
      f'~{bin(5)} = 5\n{bin(bite_a_not)} = {bite_a_not}\n\n'
      f'~{bin(5)} = 6\n{bin(bite_b_not)} = {bite_b_not}\n\n'

      f'Побитовое сдвиг влево на 2: Умножает число на 4 сдвигая биты влево \n'
      f'<<{bin(5)} = 5\n {bin(bite_rshift)} = {bite_rshift}\n\n'

      f'Побитовое сдвиг вправо на 2: целочисленно делит число на 4 сдвигая биты вправо \n'
      f'<<{bin(5)} = 5\n   {bin(bite_lshift)} = {bite_lshift}\n\n'
      )

"""
3. По введенным пользователем координатам двух точек
вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""


# _______________________________________________________________
def is_a_number(x):
    for i, el in enumerate(x):
        if not el.isdigit():
            print(f'Введите число вместо "{el}"')


# ________________________________________________________________

a1 = [i for i in input("Введи координаты A1(x1:y1): ").split()]
a2 = [i for i in input("Введи координаты A2(x2:y2): ").split()]

is_a_number(a1)
is_a_number(a2)

if a1 == a2:
    print("Координаты не могут совпадать")

if a1[0] != a2[0] or a1[1] != a2[1]:
    a1 = [int(el) for el in a1]
    a2 = [int(el) for el in a2]

    k = (a2[1] - a1[1]) / (a2[0] - a1[0])
    b = (a2[0] * a1[1] - a1[0] * a2[1]) / (a2[0] - a1[0])
    if b >= 0:
        print(f'Уравнение прямой имеет вид y = {k}x+{b}')
    else:
        print(f'Уравнение прямой имеет вид y = {k}x{b}')
else:
    print(f'Уравнение прямой имеет вид y = {a1[0]}')

"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
....
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""
import random
# ________________________________________________________________
def rand_int(new_list):
    for i, el in enumerate(new_list):
        if not el.isdigit():
            return "Введен некорректное значение диапазона"
    else:
        start = int(new_list[0])
        end = int(new_list[1])
        rez_int = random.randint(start, end)
        return rez_int


def rand_uni(new_list):
    for i, el in enumerate(new_list):
        if not el.isdigit():
            return "Введен некорректное значение диапазона"
    else:
        start = int(new_list[0])
        end = int(new_list[1])
        rez_uni = random.uniform(start, end)
        return rez_uni


def rand_char(new_list):
    for i, el in enumerate(new_list):
        if el.isdigit():
            return "Введен некорректное значение диапазона"
    else:
        start = new_list[0]
        end = new_list[1]
        rez_uni = chr(random.randint(ord(start), ord(end)))
        return rez_uni
# ________________________________________________________________


print(rand_int([i for i in input("Для поиска случайного целого числа введи диапазон через пробел ").split()]))
print(rand_uni([i for i in input("Для поиска случайного вещественного числа введи диапазон через пробел ").split()]))
print(rand_char([i for i in input("Для поиска случайного символа из алфавита введи диапазон через пробел ").split()]))


"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


def letters_in_abc(new_list):
    coord = []
    for i, el in enumerate(new_list):
        if el.isdigit():
            return "Введите букву"

    for i, el in enumerate(new_list):
        letter = str(el).lower()
        pos = ord(letter) - 96
        coord.append(pos)
    return coord

def dist():
    letters_in_abc(letters)
    distance = abs(letters_in_abc(letters)[0] - letters_in_abc(letters)[1]) - 1
    return distance


letters = [i for i in input("Введи две любые буквы Латинского алфавита через пробел").split()]
print(f"Позиция первой Буквы {letters_in_abc(letters)[0]}, Позиция второй буквы {letters_in_abc(letters)[1]},"
      f" Между буквами {dist()} символов")
