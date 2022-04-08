number_of_chrysanthemum = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
festival_day = input()

number_of_all_flowers = number_of_chrysanthemum + number_of_roses + number_of_tulips

chrysanthemum_price = 0
roses_price = 0
tulip_price = 0

if season == "Summer" or season == "Spring":
    chrysanthemum_price = number_of_chrysanthemum * 2.00
    roses_price = number_of_roses * 4.10
    tulip_price = number_of_tulips * 2.50
    if festival_day == "N":
        chrysanthemum_price = chrysanthemum_price
        roses_price = roses_price
        tulip_price = tulip_price
    elif festival_day == "Y":
        chrysanthemum_price += chrysanthemum_price * 0.15
        roses_price += roses_price * 0.15
        tulip_price += tulip_price * 0.15

elif season == "Winter" or season == "Autumn":
    chrysanthemum_price = number_of_chrysanthemum * 3.75
    roses_price = number_of_roses * 4.50
    tulip_price = number_of_tulips * 4.15
    if festival_day == "N":
        chrysanthemum_price = chrysanthemum_price
        roses_price = roses_price
        tulip_price = tulip_price
    elif festival_day == "Y":
        chrysanthemum_price += chrysanthemum_price * 0.15
        roses_price += roses_price * 0.15
        tulip_price += tulip_price * 0.15

all_flowers_price = chrysanthemum_price + roses_price + tulip_price

if number_of_tulips > 7 and season == "Spring":
    all_flowers_price -= all_flowers_price * 0.05

if number_of_roses >= 10 and season == "Winter":
    all_flowers_price -= all_flowers_price * 0.1

if number_of_all_flowers > 20:
    all_flowers_price -= all_flowers_price * 0.2

total_bill = all_flowers_price + 2

print(f"{total_bill:.2f}")



