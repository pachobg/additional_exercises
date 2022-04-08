sectors = input()
rows_sector_a = int(input())
number_of_seats = int(input())
start_seats = 0
seat_counter = 0
total_seats = 0
for sector in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if sector > sectors:
        break
    for row in range(1, rows_sector_a + 1):
        seat_counter = 0
        if row % 2 != 0:
            start_seats = number_of_seats
        elif row % 2 == 0:
            start_seats += 2
        for seat in "abcdefghijklmnopqrstuvwxyz":
            seat_counter += 1
            if seat_counter > start_seats:
                break
            total_seats += 1
            print(f"{sector}{row}{seat}")
    rows_sector_a += 1
print(total_seats)
