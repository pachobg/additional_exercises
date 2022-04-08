from math import floor, ceil

magnolia_numbers = int(input())
hyacinth_numbers = int(input())
rose_numbers = int(input())
cactus_numbers = int(input())
present_price = float(input())


magnolia_price = magnolia_numbers * 3.25
hyacinth_price = hyacinth_numbers * 4
rose_price = rose_numbers * 3.50
cactus_price = cactus_numbers * 8

all_order_cost = magnolia_price + hyacinth_price + rose_price + cactus_price

tax = all_order_cost * 0.05

profit = all_order_cost - tax

difference = abs(present_price - profit)
if profit >= present_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
