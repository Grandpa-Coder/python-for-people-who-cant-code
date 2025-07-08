customer_age = 15

while customer_age < 18:
    print("You must be 18 or older to proceed.")
    age_as_text = input("Please enter your age: ")
    customer_age = int(age_as_text)  # This is the "escape hatch"!

print(f"Age confirmed: {customer_age}. Welcome aboard!")