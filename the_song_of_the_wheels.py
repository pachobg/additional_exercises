n = int(input())
four_counter = 0
secret_pass = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                sum_abcd = a * b + c * d
                if sum_abcd == n and a < b and c > d:
                    four_counter += 1
                    print(f"{a}{b}{c}{d} ", end="")
                    if four_counter == 4:
                        secret_pass = f"{a}{b}{c}{d}"
print()
if secret_pass == 0:
    print("No!")
else:
    print(f"Password: {secret_pass}")