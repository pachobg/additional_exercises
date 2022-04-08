budget = float(input())
category = input()
number_of_fans = int(input())

price = 0
budget_left = 0

if 1 <= number_of_fans <= 4:
    budget_left = budget * 0.25
elif 5 <= number_of_fans <= 9:
    budget_left = budget * 0.4
elif 10 <= number_of_fans <= 24:
    budget_left = budget * 0.5
elif 25 <= number_of_fans <= 49:
    budget_left = budget * 0.6
elif number_of_fans >= 50:
    budget_left = budget * 0.75

if category == "VIP":
    price = number_of_fans * 499.99
elif category == "Normal":
    price = number_of_fans * 249.99

difference = abs(budget_left - price)

if price <= budget_left:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")