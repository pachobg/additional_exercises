vegetable_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

vegetable_price = vegetable_price_per_kg * vegetable_kg
fruit_price = fruit_price_per_kg * fruit_kg

total = vegetable_price + fruit_price
leva_to_euro = total / 1.94

print(f"{leva_to_euro:.2f}")