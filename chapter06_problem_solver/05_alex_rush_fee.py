def alex_rush_fee(base_cost):
    rush_amount = base_cost * 0.50
    print(f"Rush job fee (50%): ${rush_amount:.2f}")
    print("(Emergency consulting: because your poor planning is my opportunity)")

# This worked fine and made Alex feel clever
alex_rush_fee(1500.00)

# But this crashed spectacularly when Alex tried to use it!
project_base = 1500.00
rush_charge = alex_rush_fee(project_base)
total_cost = project_base + rush_charge  # BOOM! Error here!
print("Alex's confidence: also crashed")