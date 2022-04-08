letter_1 = input()
letter_2 = input()
letter_3 = input()

acs_1 = ord(letter_1)
acs_2 = ord(letter_2)
acs_3 = ord(letter_3)
combinations = 0
for i in range(acs_1, acs_2 + 1):
    for j in range(acs_1, acs_2 + 1):
        for k in range(acs_1, acs_2 + 1):
            if i == acs_3 or j == acs_3 or k == acs_3:
                pass
            else:
                combinations += 1
                print(f"{chr(i)}{chr(j)}{chr(k)} ", end="")
print(combinations)
