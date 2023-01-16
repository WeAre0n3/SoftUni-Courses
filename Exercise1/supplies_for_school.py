pen_packs = int(input())
marker_packs = int(input())
cleaner = int(input())
discount = int(input())

price_of_pens = pen_packs * 5.80
price_of_markers = marker_packs * 7.20
price_of_cleaner = cleaner * 1.20

total_price = price_of_pens + price_of_markers + price_of_cleaner

price_discount = total_price * (discount / 100)
total_sum = total_price - price_discount

print(total_sum)