order_total = 75
customer_number = 50
is_return_customer = True

if order_total >= 50:
    print("Free shipping applied!")
elif customer_number % 10 == 0:
    print("Congratulations! You're customer #50. Here's a special discount!")
elif is_return_customer:
    print("Welcome back! Loyalty discount applied.")