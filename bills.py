months = int(input())

water = 20
internet = 15
electricity_bill = 0
other_bill = 0
total_bill = 0
for month in range(1, months + 1):
    current_electricity = float(input())
    electricity_bill += current_electricity
    current_costs = current_electricity + water + internet
    other_costs = current_costs + current_costs * 0.2
    other_bill += other_costs
    total = current_costs + other_costs
    total_bill += total


water_bill = water * months
internet_bill = months * internet
average = total_bill / months


print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average:.2f} lv")