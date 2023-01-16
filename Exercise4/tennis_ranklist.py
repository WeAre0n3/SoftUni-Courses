from math import floor
number_tournaments = int(input())
starting_points = int(input())

total_points = starting_points
points_won = 0
tournaments_won = 0
for n in range(1, number_tournaments +1):
    reached_stage = str(input())
    if reached_stage == "W":
        total_points += 2000
        points_won += 2000
        tournaments_won += 1
    elif reached_stage == "F":
        total_points += 1200
        points_won += 1200
    elif reached_stage == "SF":
        total_points += 720
        points_won += 720

average_points = floor(points_won / number_tournaments)
average_win_points = (tournaments_won / number_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{average_win_points:.2f}%")
