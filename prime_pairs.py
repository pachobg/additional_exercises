start_range_first_pair = int(input())
start_range_second_pair = int(input())
stop_range_first_pair = int(input()) + start_range_first_pair
stop_range_second_pair = int(input()) + start_range_second_pair

for num1 in range(start_range_first_pair, stop_range_first_pair + 1):
    for num2 in range(start_range_second_pair, stop_range_second_pair + 1):
        if num1 % 2 != 0 and num1 % 3 != 0 and num1 % 5 != 0 and num1 % 7 != 0:
            if num2 % 2 != 0 and num2 % 3 != 0 and num2 % 5 != 0 and num2 % 7 != 0:
                print(f"{num1}{num2}")