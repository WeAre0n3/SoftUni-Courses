tabs = int(input())
salary = int(input())

remaining_money = salary

for e in range(1, tabs +1):
    website = str(input())
    if website == "Facebook":
        remaining_money -= 150
    elif website == "Instagram":
        remaining_money -= 100
    elif website == "Reddit":
        remaining_money -= 50
    if remaining_money == 0:
        print("You have lost your salary.")
        break

if remaining_money > 0:
    print(f"{remaining_money}")
