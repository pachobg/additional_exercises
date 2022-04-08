number_of_students = int(input())

total_grade = 0
top_students = 0
very_good_students = 0
good_students = 0
fail_students = 0


for student in range(1, number_of_students + 1):
    current_grade = float(input())
    if current_grade >= 5.00:
        top_students += 1
        total_grade += current_grade
    elif 4.00 <= current_grade <= 4.99:
        very_good_students += 1
        total_grade += current_grade
    elif 3.00 <= current_grade <= 3.99:
        good_students += 1
        total_grade += current_grade
    if current_grade < 3:
        fail_students += 1
        total_grade += current_grade

average_grade = total_grade / number_of_students

average_top = top_students / number_of_students * 100
average_very_good = very_good_students / number_of_students * 100
average_good = good_students / number_of_students * 100
average_fail = fail_students / number_of_students * 100

print(f"Top students: {average_top:.2f}%")
print(f"Between 4.00 and 4.99: {average_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {average_good:.2f}%")
print(f"Fail: {average_fail:.2f}%")
print(f"Average: {average_grade:.2f}")

