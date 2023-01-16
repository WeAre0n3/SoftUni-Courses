from sys import maxsize

min_num = maxsize

while True:
    number = input()
    if number == "Stop":
        break
    number = int(number)
    if number < min_num:
        min_num = number

print(min_num)
