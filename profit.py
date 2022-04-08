coins_1 = int(input())
coins_2 = int(input())
banknotes_5 = int(input())
money = int(input())

for i in range(0, coins_1 + 1):
    for j in range(0, coins_2 + 1):
        for k in range(0, banknotes_5 + 1):
            sum_i_j_k = i * 1 + j * 2 + k * 5
            if sum_i_j_k == money:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {money} lv.")
