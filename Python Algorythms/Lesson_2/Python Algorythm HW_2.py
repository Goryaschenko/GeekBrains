"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений.

Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""
import random

while True:
    maze = input("Введи выражение в формате A + B Через пробел: ").split()

    a = float(maze[0])
    b = float(maze[2])
    sign = maze[1]

    match sign:
        case "0":
            print(f'Программа расчета завершена')
            break
        case "+":
            print(f"{a} {sign} {b} = {a+b}")
        case "-":
            print(f"{a} {sign} {b} = {a - b}")
        case "*":
            print(f"{a} {sign} {b} = {a * b}")
        case "/":
            if b == 0:
                print("Деление на 0 не определено")
                continue
            print(f"{a} {sign} {b} = {a / b}")

"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def even_odd(number):
    even = 0
    odd = 0
    for i, el in enumerate(number):
        if int(el) % 2 == 0:
            even += 1
        else:
            odd += 1
    return print(f"Четных чисел {even}, Нечетных {odd}")


even_odd(input("Введи произвольное целое положительное число:"))


"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""


def reverse(number):
    a = list(number)
    a.reverse()
    rev = ''.join(a)
    return print(rev)


reverse(input("Введи произвольное целое положительное число:"))


"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def recursion(n):
    summ = 0
    maze = []
    j = 1

    if n == 1:
        return n
    else:
        for i in range(n):
            j = -0.5 * j
            summ += j
            maze.append(j)
        print(f'Сумма чиесел последовательности чисел {maze}')
        return summ


print(recursion(int(input("Введи длину последовательности:"))))

"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
from prettytable import PrettyTable

x = PrettyTable()


def generator(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


asc = []
for i in range(32, 128):
    sim = '{} : "{}"'.format(i, chr(i))
    asc.append(sim)

rows = list(generator(asc, 10))

for row in rows:
    for x in row:
        print("%10s" % (x), end="   ")
    print()


"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
import random


def is_right(answer, rand_number, nom_of_try):
    global check_winner
    check_winner = 0
    if answer > rand_number:
        return print(f"Ваше число больше загаданного, осталось {10 - int(nom_of_try)} попыток")
    elif answer < rand_number:
        return print(f"Ваше число меньше загаданного, осталось {10 - int(nom_of_try)} попыток")
    elif answer == rand_number:
        print(f"Вы угадали загаданное число было {rand_number},\n"
              f"Количество попыток: {int(nom_of_try) + 1}")
        check_winner = 1
        return check_winner


number = random.randint(0, 100)
print(number)
for nom_of_try in range(10):
    is_right(int(input("Вееди число")), number, nom_of_try)
    if check_winner == 1:
        break


"""
7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def set_of_nat(num):
    sum_of_numb = 0
    for i in range(1, num + 1):
        sum_of_numb += i
    func = num * (num + 1) / 2
    print(f"Сумма чисел = {sum_of_numb}")
    print(f"n(n+1)/2 = {func}\n"
          f"Где n = {num}")


set_of_nat(int(input("Введи количество натуральных чисел n = ")))
"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def how_much(subs, number):
    flag = 0
    mas = [int(a) for a in str(subs)]
    for i in mas:
        if i == number:
            flag += 1
    return print(f"Количество {number} в {subs} = {flag}")


how_much(input("Введи произвольное положительно число"), int(input("Введи искомое число")))

"""
9 Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
 Вывести на экран это число и сумму его цифр.
"""


def sum_of_num(num_maze):
    print(f"Ваш ряд чисел: {num_maze}")

    for item in num_maze:
        sum_i = sum(map(int, str(item)))
        sum_maze = 0
        if sum_i > sum_maze:
            sum_maze = sum_i
    print(f"Большее по сумме цифр число:{item}, Суммы его цифр = {sum_maze}")


sum_of_num(input("Введи несколько произвольных положительных целых чисел через пробел: ").split())
