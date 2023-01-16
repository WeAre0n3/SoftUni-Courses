jury_num = int(input())

total_grade = 0
presentation_counter = 0
while True:
    presentation = input()
    if presentation == "Finish":
        break
    presentation_counter += 1
    presentation_total_grade = 0
    for i in range(1, jury_num + 1):
        grade = float(input())
        presentation_total_grade += grade
    total_grade += presentation_total_grade
    average_presentation = presentation_total_grade / jury_num
    print(f"{presentation} - {average_presentation:.2f}.")


average_total = (total_grade / presentation_counter) / jury_num
print(f"Student's final assessment is {average_total:.2f}.")
