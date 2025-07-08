inventory = [
    {"product_id": "P001", "name": "Laptop", "stock": 10, "price": 1200.00},
    {"product_id": "P002", "name": "Monitor", "stock": 5, "price": 300.00},
    {"product_id": "P003", "name": "Webcam", "stock": 25, "price": 75.00}
]

print("Current Inventory:")
for product_item in inventory:
    print(f"  ID: {product_item['product_id']}, Name: {product_item['name']}, Stock: {product_item['stock']}")

# Reduce stock for "Webcam" when someone buys one
for product_item in inventory:
    if product_item["name"] == "Webcam":
        product_item["stock"] -= 1
        print(f"\nUpdated Webcam Stock: {product_item['stock']}")
        break