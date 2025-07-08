# Start with 5 items in stock
items_in_stock = 5

# Keep selling as long as there are items in stock
while items_in_stock > 0:
    print(f"Selling one item. {items_in_stock} remaining.")
    items_in_stock -= 1  # This is shorthand for: items_in_stock = items_in_stock - 1

print("All items sold! Time to restock!")