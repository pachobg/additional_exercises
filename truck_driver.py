season = input()
kilometers_per_mount = float(input())

money = 0

if season == "Autumn" or season == "Spring":
    if kilometers_per_mount <= 5000:
        money = kilometers_per_mount * 0.75
    elif 5000 < kilometers_per_mount <= 10000:
        money = kilometers_per_mount * 0.95
    elif kilometers_per_mount > 10000:
        money = kilometers_per_mount * 1.45
elif season == "Summer":
    if kilometers_per_mount <= 5000:
        money = kilometers_per_mount * 0.90
    elif 5000 < kilometers_per_mount <= 10000:
        money = kilometers_per_mount * 1.10
    elif kilometers_per_mount > 10000:
        money = kilometers_per_mount * 1.45
elif season == "Winter":
    if kilometers_per_mount <= 5000:
        money = kilometers_per_mount * 1.05
    elif 5000 < kilometers_per_mount <= 10000:
        money = kilometers_per_mount * 1.25
    elif kilometers_per_mount > 10000:
        money = kilometers_per_mount * 1.45

season_money = money * 4
government_tax = season_money * 0.1
salary = season_money - government_tax

print(f"{salary:.2f}")
