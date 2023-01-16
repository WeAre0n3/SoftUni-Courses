import math

paint_buckets = int(input())
wallpaper_roll = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_buckets_price = 21.50 * paint_buckets
wallpaper_roll_price = 5.20 * wallpaper_roll

num_gloves = math.ceil(wallpaper_roll * 35 / 100)
num_brushes = math.floor(paint_buckets * 48 / 100)

gloves_total_price = gloves_price * num_gloves
brushes_total_price = brush_price * num_brushes

total_sum = paint_buckets_price + wallpaper_roll_price + gloves_total_price + brushes_total_price

delivery_price = total_sum / 15

print(f"This delivery will cost {delivery_price:.2f} lv.")
