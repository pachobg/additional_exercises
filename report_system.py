budget_to_hit = int(input())

payment_count = 0
card_payment = 0
card_money = 0
cash_payment = 0
cash_money = 0
total = 0

command = input()

while command != "End":
    current = int(command)
    payment_count += 1
    if payment_count % 2 == 0:
        if current >= 10:
            card_payment += 1
            card_money += current
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if 0 < current <= 100:
            cash_payment += 1
            cash_money += current
            print("Product sold!")
        else:
            print("Error in transaction!")
    total = card_money + cash_money
    if total >= budget_to_hit:
        break
    command = input()
else:
    print("Failed to collect required money for charity.")


if total >= budget_to_hit:
    average_cash = cash_money / cash_payment
    average_card = card_money / card_payment
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")







