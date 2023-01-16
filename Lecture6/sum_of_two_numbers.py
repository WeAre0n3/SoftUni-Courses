interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_counter = 0
is_equal = False
for a in range(interval_start, interval_end + 1):
    for b in range(interval_start, interval_end + 1):
        combination_counter += 1
        if a + b == magic_number:
            is_equal = True
            print(f"Combination N:{combination_counter} ({a} + {b} = {magic_number})")
            break
    if is_equal:
        break

if not is_equal:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
