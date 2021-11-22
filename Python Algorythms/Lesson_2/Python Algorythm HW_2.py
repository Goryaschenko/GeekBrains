"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений.

Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""

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
