age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money = 0
saved_money = 0
toy_count = 0
brother_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += 10
        saved_money += money
        brother_count += 1
    else:
        toy_count += 1

total_sum = (saved_money - brother_count) + (toy_price * toy_count)

diff = washing_machine_price - total_sum
remaining = total_sum - washing_machine_price

if total_sum >= washing_machine_price:
    print(f"Yes! {remaining:.2f}")
else:
    print(f"No! {diff:.2f}")
