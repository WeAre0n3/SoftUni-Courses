vacation_money = float(input())
available_money = float(input())

remaining_money = available_money
days = 0
spending_days = 0

while remaining_money < vacation_money and spending_days < 5:
    action = input()
    used_sum = input()
    days += 1
    if action == "save":
        remaining_money += float(used_sum)
        spending_days = 0
    elif action == "spend":
        spending_days += 1
        remaining_money -= float(used_sum)
        if remaining_money < 0:
            remaining_money = 0

if spending_days == 5:
    print("You can't save the money.")
    print(f"{days}")

if remaining_money >= vacation_money:
    print(f"You saved the money for {days} days.")
