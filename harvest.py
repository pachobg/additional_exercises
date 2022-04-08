from math import floor, ceil
grape_plant = int(input())
grape_kg_per_m2 = float(input())
litters_needed = int(input())
number_of_workers = int(input())

all_harvest = grape_plant * grape_kg_per_m2
wine_harvest = all_harvest * 0.4

wine_litters = wine_harvest / 2.5

if wine_litters < litters_needed:
    difference = litters_needed - wine_litters
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
else:
    wine_left = wine_litters - litters_needed
    litters_wine_per_worker = wine_left / number_of_workers
    print(f"Good harvest this year! Total wine: {floor(wine_litters)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(litters_wine_per_worker)} liters per person.")