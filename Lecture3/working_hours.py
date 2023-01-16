hour = int(input())
day_of_the_week = str(input())

if day_of_the_week in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]:
    if hour in [10,11,12,13,14,15,16,17,18]:
        print("open")
    else:
        print("closed")

else:
    print("closed")