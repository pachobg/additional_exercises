n = int(input())

combinations = 0

for number_1 in range(1, n + 1):
    for number_2 in range(1, n + 1):
        print(f"{number_1}{number_2} ", end="")
        combinations += 1
print()

print(combinations)
