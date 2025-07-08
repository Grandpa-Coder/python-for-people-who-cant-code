def alex_calculate_tax(project_cost, tax_rate, state_name):
    tax_amount = project_cost * (tax_rate / 100)
    total_with_tax = project_cost + tax_amount
    
    print(f"Project Cost: ${project_cost:.2f}")
    print(f"{state_name} Tax ({tax_rate}%): ${tax_amount:.2f}")
    print(f"Total: ${total_with_tax:.2f}")
    print(f"(Thanks, {state_name}, for keeping accountants employed)")

# Alex's different client scenarios (with commentary)
print("Sarah's Bakery (Local - 8.5% tax):")
alex_calculate_tax(2500.00, 8.5, "Local")
print("\nMetro Hardware (State #2 - 6.25% tax):")
alex_calculate_tax(1800.00, 6.25, "Texas")
print("\nJohnson Dental (State #3 - 7.0% tax):")
alex_calculate_tax(3200.00, 7.0, "Florida")