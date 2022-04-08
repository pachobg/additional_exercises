budget = float(input())
season = input()

accommodation = ""
destination = ""
price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        destination = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    if season == "Summer":
        destination = "Alaska"
    elif season == "Winter":
        destination = "Morocco"
    price = budget * 0.90

print(f"{destination} - {accommodation} - {price:.2f}")
