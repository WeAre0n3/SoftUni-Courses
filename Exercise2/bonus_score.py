points = int(input())

extra_bonus = 0
if points <= 100:
    bonus = 5
elif 1000 >= points > 100:
    bonus = points * 0.2
else:
    bonus = points * 0.1

if points % 2 == 0:
    extra_bonus = 1
elif points % 10 == 5:
    extra_bonus = 2

print(bonus + extra_bonus)
print(points + bonus + extra_bonus)
