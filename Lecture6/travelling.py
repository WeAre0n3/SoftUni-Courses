while True:
    destination = input()
    if destination == "End":
        break
    min_budget = float(input())
    saved_money = 0

    while True:
        saving = float(input())
        saved_money += saving
        if saved_money >= min_budget:
            print(f"Going to {destination}!")
            saved_money = 0
            break
