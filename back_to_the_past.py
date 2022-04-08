legacy = float(input())
years_in = int(input())

age = 18
money_need = 0

for year in range(1800, years_in + 1):
    if year % 2 == 0:
        money_need += 12000
    else:
        add_money = 12000 + (age * 50)
        money_need += add_money
    age += 1

money_left = abs(legacy - money_need)

if legacy >= money_need:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {money_left:.2f} dollars to survive.")
