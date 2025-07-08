# Generate a simple pricing table
products = ["Basic", "Premium", "Enterprise"]
quantities = [1, 5, 10]

print("PRICING TABLE")
print("=" * 40)  # This creates a line of 40 equal signs - fancy!

for product in products:
    print(f"\n{product} Package:")
    for qty in quantities:
        if product == "Basic":
            price_per_unit = 10
        elif product == "Premium":
            price_per_unit = 25
        else:  # Enterprise
            price_per_unit = 50
        
        total = price_per_unit * qty
        print(f"  {qty} units: ${total}")