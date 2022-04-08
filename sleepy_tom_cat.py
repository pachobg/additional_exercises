holiday = int(input())

work_days = 365 - holiday
play_minutes = work_days * 63 + holiday * 127

if play_minutes < 30000:
    difference = 30000 - play_minutes
    hours = difference // 60
    minutes = difference % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    difference = play_minutes - 30000
    hours = difference // 60
    minutes = difference % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
