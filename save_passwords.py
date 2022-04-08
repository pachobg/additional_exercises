a = int(input())
b = int(input())
pass_number = int(input())
n = 35
m = 64
combinations = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if combinations == pass_number:
            break
        print(f"{chr(n)}{chr(m)}{i}{j}{chr(m)}{chr(n)}|", end="")
        n += 1
        m += 1
        if n > 55:
            n = 35
        if m > 96:
            m = 64
        combinations += 1
