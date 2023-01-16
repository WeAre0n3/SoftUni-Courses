input_num = input()

prime_sum = 0
non_prime_sum = 0

while input_num != "stop":
    current_num = int(input_num)

    if current_num < 0:
        print("Number is negative.")
        input_num = input()
        continue

    count = 0
    for i in range(1, current_num + 1):
        if current_num % i == 0:
            count += 1

    if count == 2:
        prime_sum += current_num
    else:
        non_prime_sum += current_num

    input_num = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
