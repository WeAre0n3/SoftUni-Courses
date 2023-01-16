yearly_fee = int(input())

shoes_price = yearly_fee - (yearly_fee * 0.40)
clothes_price = shoes_price - (shoes_price * 0.20)
ball_price = clothes_price / 4
accessories_price = ball_price / 5
total_price = yearly_fee + shoes_price + clothes_price + ball_price + accessories_price
print(total_price)
