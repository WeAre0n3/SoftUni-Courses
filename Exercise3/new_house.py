flower = str(input())
number_of_flowers = int(input())
budget = int(input())
price = 0
final_price = 0
if flower == "Roses":
    price = number_of_flowers * 5
    if number_of_flowers > 80:
        final_price = price - (price * 0.10)
    elif number_of_flowers <= 80:
        final_price = price
elif flower == "Dahlias":
    price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        final_price = price - (price * 0.15)
    elif number_of_flowers <= 90:
        final_price = price
elif flower == "Tulips":
    price = number_of_flowers * 2.80
    if number_of_flowers > 80:
        final_price = price - (price * 0.15)
    elif number_of_flowers <= 80:
        final_price = price
elif flower == "Narcissus":
    price = number_of_flowers * 3
    if number_of_flowers < 120:
        final_price = price + (price * 0.15)
    elif number_of_flowers >= 120:
        final_price = price
elif flower == "Gladiolus":
    price = number_of_flowers * 2.50
    if number_of_flowers < 80:
        final_price = price + (price * 0.20)
    elif number_of_flowers >= 80:
        final_price = price
remainder = budget - final_price
required = final_price - budget
if budget >= final_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {remainder:.2f} leva left.")
elif final_price > budget:
    print(f"Not enough money, you need {required:.2f} leva more.")
