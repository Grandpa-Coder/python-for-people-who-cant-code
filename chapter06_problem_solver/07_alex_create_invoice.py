def alex_create_invoice(client_name, hours_worked, hourly_rate, materials_cost, 
                       tax_rate, discount_percent, is_rush_job):
    print(f"Creating invoice for {client_name}...")
    print("(Please hold while Alex's computer does the math Alex used to do badly)")
    
    # Calculate labor charges
    labor_total = hours_worked * hourly_rate
    
    # Add rush job fee if needed (because someone always needs it yesterday)
    if is_rush_job:
        rush_fee = labor_total * 0.50
        print(f"Adding 50% rush fee (someone didn't plan ahead!)")
        labor_total = labor_total + rush_fee
    
    # Calculate subtotal
    subtotal = labor_total + materials_cost
    
    # Apply client discount if any
    discount_amount = subtotal * (discount_percent / 100)
    subtotal_after_discount = subtotal - discount_amount
    
    # Calculate tax (the government's cut, as always)
    tax_amount = subtotal_after_discount * (tax_rate / 100)
    
    # Calculate final total
    final_total = subtotal_after_discount + tax_amount
    
    print("(Math completed successfully! Alex is still impressed by this)")
    
    # Return all the important numbers Alex needs
    return labor_total, subtotal, discount_amount, subtotal_after_discount, tax_amount, final_total

# Alex uses it for Sarah's Bakery project (no rush job, thankfully)
labor, subtotal, discount, discounted_subtotal, tax, total = alex_create_invoice(
    "Sarah's Bakery", 20, 125.00, 450.00, 8.5, 10, False
)

print("\n" + "="*40)
print("ALEX'S BUSINESS SOLUTIONS")
print("(Professional consulting with a side of personality)")
print("Invoice for Sarah's Bakery")
print("="*40)
print(f"Consulting (20 hrs @ $125/hr): ${labor:.2f}")
print(f"Materials & Software: ${450.00:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Loyalty Discount (10%): -${discount:.2f}")
print(f"  (Because Sarah brings cookies to meetings)")
print(f"Subtotal after discount: ${discounted_subtotal:.2f}")
print(f"Tax (8.5%): ${tax:.2f}")
print(f"  (The government's favorite line item)")
print("="*40)
print(f"TOTAL DUE: ${total:.2f}")
print("(Payment in cookies also accepted)")