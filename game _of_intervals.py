moves = int(input())

points = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n_fail = 0
for move in range(1, moves + 1):
    n = int(input())
    if 0 <= n <= 9:
        n1 += 1
        points = points + n * 0.20
    elif 10 <= n <= 19:
        n2 += 1
        points = points + n * 0.30
    elif 20 <= n <= 29:
        n3 += 1
        points = points + n * 0.40
    elif 30 <= n <= 39:
        n4 += 1
        points += 50
    elif 40 <= n <= 50:
        n5 += 1
        points += 100
    else:
        points = points / 2
        n_fail += 1

n1_percent = n1 / moves * 100
n2_percent = n2 / moves * 100
n3_percent = n3 / moves * 100
n4_percent = n4 / moves * 100
n5_percent = n5 / moves * 100
n_fail_percent = n_fail / moves * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {n1_percent:.2f}%")
print(f"From 10 to 19: {n2_percent:.2f}%")
print(f"From 20 to 29: {n3_percent:.2f}%")
print(f"From 30 to 39: {n4_percent:.2f}%")
print(f"From 40 to 50: {n5_percent:.2f}%")
print(f"Invalid numbers: {n_fail_percent:.2f}%")
