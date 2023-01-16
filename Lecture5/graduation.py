name = input()

passed_years = 0
failed_years = 0
total_grade = 0


while True:
    grade = float(input())
    passed_years += 1

    if grade < 4:
        failed_years += 1
        if failed_years == 2:
            print(f"{name} has been excluded at {passed_years} grade")
            break
        passed_years -= 1
    else:
        total_grade += grade

    if passed_years == 12:
        average_grade = total_grade / passed_years
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
