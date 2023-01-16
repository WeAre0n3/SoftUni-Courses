actor = str(input())
academy_points = float(input())
n = int(input())

total_points = academy_points

for i in range(1, n + 1):
    score_giver = str(input())
    points = float(input())
    total_points += (len(score_giver) * points) / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break


if total_points <= 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor} you need {diff:.1f} more!")
