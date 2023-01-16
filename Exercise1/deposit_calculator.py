deposit = float(input())
duration_of_deposit = int(input())
interest_rate = float(input())

sum = deposit + duration_of_deposit * ((deposit * (interest_rate / 100)) / 12 )
print(sum)