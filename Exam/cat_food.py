num_cats = int(input())

small_cats = 0
big_cats = 0
huge_cats = 0
total_food = 0

for c in range(1, num_cats + 1):
    food_grams = float(input())
    total_food += food_grams
    if 100 <= food_grams < 200:
        small_cats += 1
    elif food_grams < 300:
        big_cats += 1
    elif food_grams < 400:
        huge_cats += 1

total_food_kg = total_food / 1000
food_price = total_food_kg * 12.45

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")
