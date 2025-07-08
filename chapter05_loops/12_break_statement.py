# Looking for a specific product in inventory
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]
target_product = "Keyboard"

for product in products:
    print(f"Checking: {product}")
    if product == target_product:
        print(f"Found it! {target_product} is in stock.")
        break  # Exit the loop immediately - no need to keep looking!
    print(f"{product} is not what we're looking for.")

print("Search complete!")