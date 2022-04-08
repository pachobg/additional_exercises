detergent_bottles = int(input())

detergent_ml = 750 * detergent_bottles

washed_dishes = 0
washed_pots = 0
load_count = 0
used_detergent = 0
detergent_ends = False

command = input()
while command != "End":
    current_utensils = int(command)
    load_count += 1
    if load_count % 3 == 0:
        washed_pots += current_utensils
        used_detergent += current_utensils * 15
        if used_detergent > detergent_ml:
            detergent_ends = True
            break
    else:
        washed_dishes += current_utensils
        used_detergent += current_utensils * 5
        if used_detergent > detergent_ml:
            detergent_ends = True
            break
    command = input()

difference = abs(detergent_ml - used_detergent)

if detergent_ends:
    print(f"Not enough detergent, {difference} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{washed_dishes} dishes and {washed_pots} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
