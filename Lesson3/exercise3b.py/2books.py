copy = int(input())
price = 24.95
ship = 3
shipping = (copy - 1) *0.75 + ship
discount = price * 0.6
discounted_price= (discount)
total_books = discounted_price * copy
total_bill = total_books + shipping
print(total_bill)



