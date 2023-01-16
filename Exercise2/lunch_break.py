from math import ceil
name_of_series = str(input())
length_of_episode = int(input())
length_of_break = int(input())

lunchtime = length_of_break / 8
time_for_rest = length_of_break / 4

if length_of_break >= lunchtime + time_for_rest + length_of_episode:
    print(f"You have enough time to watch {name_of_series} and left with "
          f"{ceil(length_of_break - (lunchtime + time_for_rest + length_of_episode))} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series},"
          f" you need {ceil((lunchtime + time_for_rest + length_of_episode) - length_of_break)} more minutes.")