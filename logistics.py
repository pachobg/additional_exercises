number_of_loads = int(input())

all_load = 0
price = 0
buss_load = 0
truck_load = 0
train_load = 0

for x in range(1, number_of_loads + 1):
    current_load = int(input())
    all_load += current_load
    if 1 <= current_load <= 3:
        buss_price = current_load * 200
        price += buss_price
        buss_load += current_load
    elif 4 <= current_load <= 11:
        truck_price = current_load * 175
        price += truck_price
        truck_load += current_load
    elif current_load >= 12:
        train_price = current_load * 120
        price += train_price
        train_load += current_load

average_price = price / all_load
average_buss_load = buss_load / all_load * 100
average_truck_load = truck_load / all_load * 100
average_train_load = train_load / all_load * 100

print(f"{average_price:.2f}")
print(f"{average_buss_load:.2f}%")
print(f"{average_truck_load:.2f}%")
print(f"{average_train_load:.2f}%")



