kilometers = int(input())
day_time = input()

price = 0

if day_time == "day":
    if kilometers < 20:
        price = 0.70 + kilometers * 0.79
    elif 20 <= kilometers < 100:
        price = 0.09 * kilometers
    elif kilometers >= 100:
        price = 0.06 * kilometers
elif day_time == "night":
    if kilometers < 20:
        price = 0.70 + kilometers * 0.9
    elif 20 <= kilometers < 100:
        price = 0.09 * kilometers
    elif kilometers >= 100:
        price = 0.06 * kilometers

print(f"{price:.2f}")
