num = int(input())

current_sum = 0

for x in range(num):
    current = int(input())
    current_sum += current

average = current_sum / num

print(f"{average:.2f}")
