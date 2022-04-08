n = int(input())
latin = int(input())
letter1_counter = 0
letter2_counter = 0
for n1 in range(1, n + 1):
    for n2 in range(1, n + 1):
        for letter1 in "abcdefghijklmnopqrstuvwxyz":
            letter1_counter += 1
            if letter1_counter > latin:
                letter1_counter = 0
                break
            for letter2 in "abcdefghijklmnopqrstuvwxyz":
                letter2_counter += 1
                if letter2_counter > latin:
                    letter2_counter = 0
                    break
                for n3 in range(1, n + 1):
                    if n3 > n1 and n3 > n2:
                        print(f"{n1}{n2}{letter1}{letter2}{n3} ", end="")
