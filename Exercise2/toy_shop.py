trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
toy_trucks = int(input())

price_puzzles = puzzles * 2.60
price_dolls = dolls * 3
price_teddy_bears = teddy_bears * 4.10
price_minions = minions * 8.20
price_toy_trucks = toy_trucks * 2
total_price = price_puzzles + price_dolls + price_teddy_bears + price_minions + price_toy_trucks
total_toy_count = puzzles + dolls + teddy_bears + minions + toy_trucks

if total_toy_count >= 50:
    total_price = total_price - (total_price * 0.25)

total_profit = total_price - (total_price * 0.1)
remainder = f"{(total_profit - trip_price):.2f}"
required = f"{(trip_price - total_profit):.2f}"

if total_profit >= trip_price:
    print(f"Yes! {remainder} lv left.")
else:
    print(f"Not enough money! {required} lv needed.")