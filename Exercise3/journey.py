budget = float(input())
season = str(input())

destination = ''
type_of_stay = ''
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == "summer":
        type_of_stay = "Camp"
        expenses = budget * 0.30
    elif season == "winter":
        type_of_stay = "Hotel"
        expenses = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        type_of_stay = "Camp"
        expenses = budget * 0.40
    elif season == "winter":
        type_of_stay = "Hotel"
        expenses = budget * 0.80
elif budget > 1000:
    destination = 'Europe'
    type_of_stay = "Hotel"
    expenses = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{type_of_stay} - {expenses:.2f}")


