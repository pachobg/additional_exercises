from math import floor
hours = int(input())
day_have = int(input())
number_of_workers = int(input())

days_for_education = day_have * 0.1
days_left = day_have - days_for_education

hours_lef = days_left * 8

overtime_work = number_of_workers * 2 * day_have

project_hours = hours_lef + overtime_work

if project_hours >= hours:
    difference = floor(project_hours) - hours
    print(f"Yes!{difference} hours left.")
else:
    difference = hours - floor(project_hours)
    print(f"Not enough time!{difference} hours needed.")

