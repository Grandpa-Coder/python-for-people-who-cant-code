inventory = {
    "Laptops": 15,
    "Mice": 47,
    "Keyboards": 23,
    "Monitors": 8,
    "Webcams": 31
}

print("LOW STOCK ALERT")
print("=" * 30)

low_stock_items = []

for item, quantity in inventory.items():  # .items() gives us both the name and quantity
    if quantity < 20:
        low_stock_items.append(item)
        print(f"⚠️  {item}: Only {quantity} left!")

if not low_stock_items:
    print("✅ All items are well-stocked! Time for a coffee break.")
else:
    print(f"\nTotal items needing restock: {len(low_stock_items)}")