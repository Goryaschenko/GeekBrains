# to contain

DISCOUNT = 9
basket = [1589.1, 7896.1, 4572.5, 2463.3] #не массив а список muttable

basket_discount = []

for price in basket:
    print(price)
    print('-' * 10)

# basket_2 = (1589.1,
#             7896.1,
#             4572.5,
#             2463.3
#             ) #Картеж immutable картеж создается запятой

#  #           0       1       2       3
#               -1      -2      -3      -1      0
# print(basket, type(basket))

# # print(basket[0])  # getter
# print(basket[-1])  # getter

# print(basket[len(basket) - 1])
# print(basket[-1])  # getter можно использовать вызов объекта массива с конца

# print(dir(basket)) #выводит все команды
# basket.append(42875.1)
# print(basket, type(basket_2))
# print(basket, type(basket))

