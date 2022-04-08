n = int(input())
k = int(input())
for n1 in range(n, k + 1):
    for n2 in range(n, k + 1):
        for n3 in range(n, k + 1):
            for n4 in range(n, k + 1):
                sum_2_3 = n2 + n3
                if n1 > n4 and n1 % 2 != 0 and sum_2_3 % 2 == 0 and n4 % 2 == 0:
                    print(f"{n1}{n2}{n3}{n4} ", end="")
                elif n1 > n4 and n1 % 2 == 0 and sum_2_3 % 2 == 0 and n4 % 2 != 0:
                    print(f"{n1}{n2}{n3}{n4} ", end="")