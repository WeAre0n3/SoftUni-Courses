quantity_of_nylon = int(input())
quantity_of_paint = int(input())
quantity_of_thinner = int(input())
number_of_hours = int(input())

price_of_nylon = (quantity_of_nylon + 2) * 1.50
price_of_paint = (quantity_of_paint + (quantity_of_paint * 0.10)) * 14.50
price_of_thinner = quantity_of_thinner * 5.00
price_of_bags = 0.40

total_sum_for_materials = price_of_thinner + price_of_bags + price_of_paint + price_of_nylon
price_for_working_1hour = total_sum_for_materials * 0.30
total_expenses = total_sum_for_materials + (price_for_working_1hour * number_of_hours)

print(total_expenses)

