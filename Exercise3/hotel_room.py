month = str(input())
number_of_days = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

total_price_studio = studio_price * number_of_days
total_price_apartment = apartment_price * number_of_days

if 7 < number_of_days <= 14 and (month == "May" or month == "October"):
    total_price_studio = total_price_studio * 0.95
elif number_of_days > 14 and (month == "May" or month == "October"):
    total_price_studio = total_price_studio * 0.70
elif number_of_days > 14 and (month == "June" or month == "September"):
    total_price_studio = total_price_studio * 0.80

if number_of_days > 14:
    total_price_apartment = total_price_apartment * 0.90

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
