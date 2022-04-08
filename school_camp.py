season = input()
group_type = input()
number_of_students = int(input())
overnights = int(input())

sport = ""
price = 0
discount = 0
if season == "Winter":
    if group_type == "girls":
        sport = "Gymnastics"
        price = number_of_students * 9.60 * overnights
    elif group_type == "boys":
        sport = "Judo"
        price = number_of_students * 9.60 * overnights
    elif group_type == "mixed":
        sport = "Ski"
        price = number_of_students * 10 * overnights

elif season == "Spring":
    if group_type == "girls":
        sport = "Athletics"
        price = number_of_students * 7.20 * overnights
    elif group_type == "boys":
        sport = "Tennis"
        price = number_of_students * 7.20 * overnights
    elif group_type == "mixed":
        sport = "Cycling"
        price = number_of_students * 9.50 * overnights

elif season == "Summer":
    if group_type == "girls":
        sport = "Volleyball"
        price = number_of_students * 15 * overnights
    elif group_type == "boys":
        sport = "Football"
        price = number_of_students * 15 * overnights
    elif group_type == "mixed":
        sport = "Swimming"
        price = number_of_students * 20 * overnights

if 1 <= number_of_students < 10:
    discount = 0
elif 10 <= number_of_students < 20:
    discount = price * 0.05
elif 20 <= number_of_students < 50:
    discount = price * 0.15
elif number_of_students >= 50:
    discount = price * 0.5

final_bill = price - discount

print(f"{sport} {final_bill:.2f} lv.")

