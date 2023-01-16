group_num = int(input())

musala_group = 0
mont_blanc_group = 0
kilimandharo_group = 0
k2_group = 0
everest_group = 0


for i in range(1, group_num + 1):
    people_per_group = int(input())
    if people_per_group <= 5:
        musala_group += people_per_group
    elif people_per_group <= 12:
        mont_blanc_group += people_per_group
    elif people_per_group <= 25:
        kilimandharo_group += people_per_group
    elif people_per_group <= 40:
        k2_group += people_per_group
    elif people_per_group > 40:
        everest_group += people_per_group

total_sum_people = musala_group + mont_blanc_group + kilimandharo_group + k2_group + everest_group

musala_climbers = musala_group / total_sum_people * 100
mon_blanc_climbers = mont_blanc_group / total_sum_people * 100
kilimandharo_climbers = kilimandharo_group / total_sum_people * 100
k2_climbers = k2_group / total_sum_people * 100
everest_climbers = everest_group / total_sum_people * 100

print(f"{musala_climbers:.2f}%")
print(f"{mon_blanc_climbers:.2f}%")
print(f"{kilimandharo_climbers:.2f}%")
print(f"{k2_climbers:.2f}%")
print(f"{everest_climbers:.2f}%")
