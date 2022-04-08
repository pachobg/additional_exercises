mackerel_price_per_kg = float(input())
sprat_fish_price_per_kg = float(input())
bonito_fish_kg = float(input())
horse_mackerel_kg = float(input())
shells_kg = int(input())

bonito_fish_price_per_kg = mackerel_price_per_kg + mackerel_price_per_kg * 0.6
bonito_price = bonito_fish_price_per_kg * bonito_fish_kg

horse_mackerel_price_per_kg = sprat_fish_price_per_kg + sprat_fish_price_per_kg * 0.8
horse_mackerel_price = horse_mackerel_price_per_kg * horse_mackerel_kg

shells_price = shells_kg * 7.50

total_price = bonito_price + horse_mackerel_price + shells_price

print(f"{total_price:.2f}")
