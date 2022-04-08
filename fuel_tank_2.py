fuel_type = input()
fuel_liters = float(input())
membership_card = input()

diesel_price = 2.33
gasoline_price = 2.22
gas_price = 0.93

bill = 0

if membership_card == "Yes":
    diesel_price -= 0.12
    gasoline_price -= 0.18
    gas_price -= 0.08

if 0 <= fuel_liters < 20:
    if fuel_type == "Diesel":
        bill = fuel_liters * diesel_price
    elif fuel_type == "Gasoline":
        bill = fuel_liters * gasoline_price
    elif fuel_type == "Gas":
        bill = fuel_liters * gas_price
elif 20 <= fuel_liters <= 25:
    if fuel_type == "Diesel":
        bill = fuel_liters * diesel_price * 0.92
    elif fuel_type == "Gasoline":
        bill = fuel_liters * gasoline_price * 0.92
    elif fuel_type == "Gas":
        bill = fuel_liters * gas_price * 0.92
elif fuel_liters > 25:
    if fuel_type == "Diesel":
        bill = fuel_liters * diesel_price * 0.9
    elif fuel_type == "Gasoline":
        bill = fuel_liters * gasoline_price * 0.9
    elif fuel_type == "Gas":
        bill = fuel_liters * gas_price * 0.9

print(f"{bill:.2f} lv.")