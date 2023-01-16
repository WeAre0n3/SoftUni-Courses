numbers = int(input())

left_sum = 0
right_sum = 0

for i in range(1, numbers + 1):
    left_sum += int(input())

for n in range(1, numbers +1, 1):
    right_sum += int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
