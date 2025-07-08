# Generate a formatted customer list
customers = ["Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson"]
print("CUSTOMER CONTACT LIST")
print("=" * 40)

for i, customer in enumerate(customers, 1):  # enumerate gives us numbers starting at 1
    print(f"{i}.\t{customer}")
    print(f"\tEmail: {customer.lower().replace(' ', '.')}@company.com")
    print(f"\tPhone: (555) 123-{1000 + i}")
    print()  # Empty line between customers