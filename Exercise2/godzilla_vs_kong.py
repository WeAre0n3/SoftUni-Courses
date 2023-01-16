budget = float(input())
extras = int(input())
costume_price = float(input())
decor = budget * 0.1

if extras > 150:
    costume_price = costume_price - (costume_price * 0.1)

total_cost = extras * costume_price + decor

remainder = f"{(budget - total_cost):.2f}"
required = f"{(total_cost - budget):.2f}"

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {required} leva more.")

if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {remainder} leva left.")
