world_record = float(input())
distance_meters = float(input())
seconds_per_travelled_meter = float(input())

time_to_finish = distance_meters * seconds_per_travelled_meter
delay = (distance_meters // 15) * 12.5

time_to_finish += delay

if time_to_finish < world_record:
    print(f" Yes, he succeeded! The new world record is {time_to_finish:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_to_finish - world_record:.2f} seconds slower.")
