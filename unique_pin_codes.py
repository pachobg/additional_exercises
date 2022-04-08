firs_number = int(input())
second_number = int(input())
third_number = int(input())

pin_code = ""

for fn in range(1, firs_number + 1):
    for sn in range(1, second_number + 1):
        for tn in range(1, third_number + 1):
            if fn % 2 == 0 and tn % 2 == 0 and (sn == 2 or sn == 3 or sn == 5 or sn == 7):
                pin_code += str(fn) + " " + str(sn) + " " + str(tn)
                print(pin_code)
                pin_code = ""