from math import floor, ceil
holiday_days = int(input())
predicted_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

total_dog_food = holiday_days * dog_food_per_day
total_cat_food = holiday_days * cat_food_per_day
total_turtle_food = holiday_days * turtle_food_per_day / 1000

total_food = total_dog_food + total_cat_food + total_turtle_food

difference = abs(predicted_food - total_food)
if predicted_food >= total_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
