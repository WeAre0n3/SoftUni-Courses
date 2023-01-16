budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

gpu_price = gpu * 250
cpu_price = cpu * (gpu_price * 0.35)
ram_price = ram * (gpu_price * 0.1)
total_price = gpu_price + cpu_price + ram_price
discount = total_price * 0.15

if gpu > cpu:
    total_price = total_price - discount

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
