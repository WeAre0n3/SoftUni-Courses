lenght_cm = int(input())
width_cm = int(input())
hight_cm = int(input())
percent = float(input())

total_aquarium_volume = lenght_cm * width_cm * hight_cm
volume_lt = total_aquarium_volume / 1000
occupied_space = percent / 100
needed_lt = volume_lt * (1 - occupied_space)
print(needed_lt)