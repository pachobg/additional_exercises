stadium_places = int(input())
number_of_fans = int(input())

fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for fan in range(1, number_of_fans + 1):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

sector_a_percent = fans_a / number_of_fans * 100
sector_b_percent = fans_b / number_of_fans * 100
sector_v_percent = fans_v / number_of_fans * 100
sector_g_percent = fans_g / number_of_fans * 100
stadium_full_percent = number_of_fans / stadium_places * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{stadium_full_percent:.2f}%")