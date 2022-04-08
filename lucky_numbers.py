n = int(input())

for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                sum_1_2 = n1 + n2
                sum_3_4 = n3 + n4
                if sum_1_2 == sum_3_4 and n % sum_1_2 == 0:
                    print(f"{n1}{n2}{n3}{n4} ", end="")
