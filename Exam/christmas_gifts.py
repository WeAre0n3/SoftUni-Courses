adults = 0
kids = 0

while True:
    num_years = input()
    if num_years == "Christmas":
        break
    else:
        num_years = int(num_years)
    if num_years <= 16:
        kids += 1
    else:
        adults += 1


total_price_toys = kids * 5
total_price_sweaters = adults * 15

print(f"Number of adults: {adults}")
print(f"Number of kids: {kids}")
print(f"Money for toys: {total_price_toys}")
print(f"Money for sweaters: {total_price_sweaters}")
