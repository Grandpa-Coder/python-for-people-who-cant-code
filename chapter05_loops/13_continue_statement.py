# Process only even numbers (skip the odd ones)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 1:  # If the number is odd (% gives us the remainder)
        continue  # Skip the rest and go to next number
    
    print(f"Processing even number: {number}")
    # More processing code would go here