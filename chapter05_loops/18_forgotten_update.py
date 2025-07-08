# Wrong: This creates an infinite loop
count = 0
while count < 5:
    print("Hello")
    # Forgot to update count! It stays 0 forever

# Right: This loop will actually end
count = 0
while count < 5:
    print("Hello")
    count += 1  # Don't forget this crucial step!