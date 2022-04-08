limit_100 = int(input())
limit_10 = int(input())
limit_1 = int(input())

for i in range(1, limit_100 + 1):
    for j in range(1, limit_10 + 1):
        for k in range(1, limit_1 + 1):
            if i % 2 == 0 and k % 2 == 0 and j == 2:
                print(f"{i} {j} {k}")
            elif i % 2 == 0 and k % 2 == 0 and j == 3:
                print(f"{i} {j} {k}")
            elif i % 2 == 0 and k % 2 == 0 and j == 5:
                print(f"{i} {j} {k}")
            elif i % 2 == 0 and k % 2 == 0 and j == 7:
                print(f"{i} {j} {k}")
