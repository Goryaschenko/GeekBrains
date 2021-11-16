'''
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

maze = list(str(input()))
a = []

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
