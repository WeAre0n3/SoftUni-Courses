n1 = int(input())
n2 = int(input())

for n in range(n1, n2 + 1):
    to_string = str(n)
    even_sum = 0
    odd_sum = 0
    for j in range(0, len(to_string)):
        digit = int(to_string[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(to_string, end=' ')
