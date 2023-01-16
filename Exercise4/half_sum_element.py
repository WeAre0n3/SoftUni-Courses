from sys import maxsize

number = int(input())

max_num = -maxsize
total_sum = 0

for n in range(0, number):
    num = int(input())
    if num > max_num:
        max_num = num
    total_sum += num

if max_num == total_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    total_sum -= max_num
    print(f"Diff = {abs(max_num - total_sum)}")
