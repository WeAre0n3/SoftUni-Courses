square_meters = float(input())
final_price = float(square_meters * 7.61)
discount = float(final_price * 0.18)

print(f"The final price is: {final_price - discount}  lv.")
print(f"The discount is: {discount} lv.")