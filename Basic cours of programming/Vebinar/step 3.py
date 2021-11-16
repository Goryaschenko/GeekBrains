# to contain

DISCOUNT = 9
basket = (1589.1, 7896.1, 4572.5, 2463.3)
basket_discount = []

for price in basket:
    basket_discount.append(price * (100 - DISCOUNT)/100)
    print(basket_discount)