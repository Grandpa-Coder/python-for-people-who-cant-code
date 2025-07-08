customer_age = 15  # Alex starts with an age less than 18
while customer_age < 18:
    print("You must be 18 or older to proceed.")
    # Alex forgot to update 'customer_age' inside the loop!
    # customer_age = int(input("Please enter your age: "))  # This crucial line was missing!