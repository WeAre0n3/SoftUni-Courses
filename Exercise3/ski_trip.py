days_stay = int(input())
room_type = str(input())
rate = str(input())

nights_stay = days_stay - 1

total_price = 0

if room_type == "room for one person":
    total_price = 18.00 * nights_stay
elif room_type == "apartment":
    total_price = 25.00 * nights_stay
    if days_stay < 10:
        total_price = total_price * 0.70
    elif 10 <= days_stay <= 15:
        total_price = total_price * 0.65
    else:
        total_price = total_price * 0.50
elif room_type == "president apartment":
    total_price = 35.00 * nights_stay
    if days_stay < 10:
        total_price = total_price * 0.90
    elif 10 <= days_stay <= 15:
        total_price = total_price * 0.85
    elif days_stay > 15:
        total_price = total_price * 0.80

if rate == "positive":
    total_price = total_price * 1.25
elif rate == "negative":
    total_price = total_price * 0.90

print(f"{total_price:.02f}")
