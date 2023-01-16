budget = int(input())
season = str(input())
number_of_fishers = int(input())
price_boat = 0

if season == "Spring":
    price_boat = 3000
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
elif season == "Winter":
    price_boat = 2600

if number_of_fishers <= 6:
    price_boat = price_boat * 0.90
elif 6 < number_of_fishers <= 11:
    price_boat = price_boat * 0.85
elif number_of_fishers > 11:
    price_boat = price_boat * 0.75

if number_of_fishers % 2 == 0 and season != "Autumn":
    price_boat = price_boat * 0.95

difference = abs(budget - price_boat)

if budget >= price_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
