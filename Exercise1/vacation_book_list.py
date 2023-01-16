pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

collective_time_to_read = pages / pages_per_hour
hours_per_day = int(collective_time_to_read // number_of_days)
print(hours_per_day)
