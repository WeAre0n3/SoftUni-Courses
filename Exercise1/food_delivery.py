number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegeterian_menus = int(input())

chicken_price = number_of_chicken_menus * 10.35
fish_price = number_of_fish_menus * 12.40
vegeterian_price = number_of_vegeterian_menus * 8.15

total_menu_price = chicken_price + fish_price + vegeterian_price
dessert = total_menu_price * 0.20
delivery = 2.50

final_price = total_menu_price + dessert + delivery
print(final_price)