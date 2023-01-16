from math import floor

width = float(input())
length = float(input())
height = float(input())
astronaut_height = float(input())

volume_spacecraft = width * length * height

volume_room = (astronaut_height + 0.40) * 2 * 2

num_astronauts = floor(volume_spacecraft / volume_room)

if 3 <= num_astronauts <= 10:
    print(f"The spacecraft holds {num_astronauts} astronauts.")
elif num_astronauts < 3:
    print(f"The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
