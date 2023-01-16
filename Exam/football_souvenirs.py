team = input()
souvenir_type = input()
num_souvenirs = int(input())

total_sum = 0

if team == "Argentina":
    if souvenir_type == "flags":
        total_sum = num_souvenirs * 3.25
    elif souvenir_type == "caps":
        total_sum = num_souvenirs * 7.20
    elif souvenir_type == "posters":
        total_sum = num_souvenirs * 5.10
    elif souvenir_type == "stickers":
        total_sum = num_souvenirs * 1.25
    else:
        print("Invalid stock!")
        exit()
elif team == "Brazil":
    if souvenir_type == "flags":
        total_sum = num_souvenirs * 4.20
    elif souvenir_type == "caps":
        total_sum = num_souvenirs * 8.50
    elif souvenir_type == "posters":
        total_sum = num_souvenirs * 5.35
    elif souvenir_type == "stickers":
        total_sum = num_souvenirs * 1.20
    else:
        print("Invalid stock!")
        exit()
elif team == "Croatia":
    if souvenir_type == "flags":
        total_sum = num_souvenirs * 2.75
    elif souvenir_type == "caps":
        total_sum = num_souvenirs * 6.90
    elif souvenir_type == "posters":
        total_sum = num_souvenirs * 4.95
    elif souvenir_type == "stickers":
        total_sum = num_souvenirs * 1.10
    else:
        print("Invalid stock!")
        exit()
elif team == "Denmark":
    if souvenir_type == "flags":
        total_sum = num_souvenirs * 3.10
    elif souvenir_type == "caps":
        total_sum = num_souvenirs * 6.50
    elif souvenir_type == "posters":
        total_sum = num_souvenirs * 4.80
    elif souvenir_type == "stickers":
        total_sum = num_souvenirs * 0.90
    else:
        print("Invalid stock!")
        exit()
else:
    print("Invalid country!")
    exit()

print(f"Pepi bought {num_souvenirs} {souvenir_type} of {team} for {total_sum:.2f} lv.")
