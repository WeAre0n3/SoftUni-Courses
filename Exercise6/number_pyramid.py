number = int(input())

num_counter = 1
stop = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if num_counter > number:
            stop = True
            break
        print(num_counter, end=' ')
        num_counter += 1
    print()
    if stop:
        break
