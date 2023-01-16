number = int(input())

total_sum = 0

while True:
    number2 = int(input())
    total_sum += number2
    if total_sum >= number:
        break

print(total_sum)
