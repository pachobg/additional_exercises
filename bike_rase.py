junior_competitors = int(input())
senior_competitors = int(input())
type_of_route = input()

all_competitors = junior_competitors + senior_competitors
junior_tax = 0
senior_tax = 0

if type_of_route == "trail":
    junior_tax = junior_competitors * 5.50
    senior_tax = senior_competitors * 7
elif type_of_route == "cross-country":
    junior_tax = junior_competitors * 8
    senior_tax = senior_competitors * 9.50
    if all_competitors >= 50:
        junior_tax = (junior_competitors * 8) * 0.75
        senior_tax = (senior_competitors * 9.50) * 0.75
elif type_of_route == "downhill":
    junior_tax = junior_competitors * 12.25
    senior_tax = senior_competitors * 13.75
elif type_of_route == "road":
    junior_tax = junior_competitors * 20
    senior_tax = senior_competitors * 21.50

tax_money = junior_tax + senior_tax

spend_fee = tax_money * 0.05

profit = tax_money - spend_fee

print(f"{profit:.2f}")
