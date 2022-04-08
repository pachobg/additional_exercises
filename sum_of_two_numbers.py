start = int(input())
end = int(input())
magic_number = int(input())
result = 0
combination = 0
true_combination = 0
is_found = False
for i in range(start, end + 1):
    for y in range(start, end + 1):
        combination += 1
        result = i + y
        if result == magic_number:
            true_combination += 1
            if true_combination == 1:
                print(f"Combination N:{combination} ({i} + {y} = {magic_number})")
            else:
                pass
if true_combination == 0:
    print(f"{combination} combinations - neither equals {magic_number}")