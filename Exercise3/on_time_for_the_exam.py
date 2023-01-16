hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

exam_all_min = (hour_of_exam * 60) + minutes_of_exam
arriving_all_min = (hour_of_arriving * 60) + minutes_of_arriving
diff = abs(exam_all_min - arriving_all_min)

if exam_all_min < arriving_all_min:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")
elif exam_all_min == arriving_all_min or diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")


