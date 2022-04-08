length_x = float(input())
width_y = float(input())
height_h = float(input())

door_area = 1.2 * 2
window_area = 2 * (1.5 * 1.5)

front_back_area = 2 * (length_x * length_x) - door_area
side_area = 2 * (length_x * width_y) - window_area
wall_area = front_back_area + side_area

roof_area = 2 * (length_x * width_y) + 2 * ((length_x * height_h) / 2)

green_paint = wall_area / 3.4

red_paint = roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
