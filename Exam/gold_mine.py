num_locations = int(input())

for l in range(1, num_locations + 1):
    average_gold = float(input())
    num_days = int(input())
    total_gold = 0
    for m in range(1, num_days + 1):
        current_gold = float(input())
        total_gold += current_gold
    average_gold_per_day = total_gold / num_days
    if average_gold_per_day >= average_gold:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        diff = average_gold - average_gold_per_day
        print(f"You need {diff:.2f} gold.")
