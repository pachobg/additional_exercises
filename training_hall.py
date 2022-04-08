w = float(input())
h = float(input())

hallway = 100
w_cm = w * 100
h_cm = h * 100
hall_h = h_cm - hallway

work_place_w = w_cm // 120
work_place_h = hall_h // 70

all_work_place = work_place_w * work_place_h - 3

print(all_work_place)
