hour = int(input())
minutes = int(input())

all_minutes = hour * 60 + minutes
all_minutes += 15

hours = all_minutes // 60
final_minutes = all_minutes % 60

if hours == 24:
    hours = 0

print(f"{hours}:{final_minutes:02d}")
