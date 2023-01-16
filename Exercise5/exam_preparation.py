poor_grades = int(input())

problems_solved = 0
poor_grades_count = 0
sum_grades = 0
last_problem = ""
has_failed = True
while poor_grades_count < poor_grades:
    current_problem = input()

    if current_problem == "Enough":
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        poor_grades_count += 1

    sum_grades += grade
    problems_solved += 1
    last_problem = current_problem

if has_failed:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    print(f"Average score: {sum_grades / problems_solved:.2f}")
    print(f"Number of problems: {problems_solved}")
    print(f"Last problem: {last_problem}")
