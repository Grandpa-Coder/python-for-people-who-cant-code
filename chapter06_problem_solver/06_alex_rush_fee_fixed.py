def alex_rush_fee(base_cost):
    rush_amount = base_cost * 0.50
    print("(Calculating the 'you needed this yesterday' surcharge)")
    return rush_amount

project_base = 1500.00
rush_charge = alex_rush_fee(project_base)
total_cost = project_base + rush_charge

print(f"Metro Hardware Rush Project:")
print(f"Base cost: ${project_base:.2f}")
print(f"Rush fee (50%): ${rush_charge:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print("(Alex's ego: slowly recovering)")