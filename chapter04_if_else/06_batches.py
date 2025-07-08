customer_count = 25

if customer_count % 10 == 0:
    print("Reached a batch of 10! Time to send welcome emails.")
elif customer_count % 5 == 0:
    print("Halfway to the next batch.")