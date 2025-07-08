def alex_calculate_client_discount(project_cost, discount_percent, reason):
    discount_amount = project_cost * (discount_percent / 100)
    print(f"Applying {discount_percent}% discount for: {reason}")
    print(f"(Alex's generosity knows some bounds, but not many)")
    return discount_amount

# Alex can now use the result in other calculations
sarahs_project_cost = 2500.00
loyalty_discount = alex_calculate_client_discount(sarahs_project_cost, 10, "loyal customer")
final_cost = sarahs_project_cost - loyalty_discount

print(f"\nSarah's Bakery Project Summary:")
print(f"Original cost: ${sarahs_project_cost:.2f}")
print(f"Loyalty discount: ${loyalty_discount:.2f}")  
print(f"Final cost: ${final_cost:.2f}")
print("(Worth every penny of lost profit for Sarah's amazing cookies)")