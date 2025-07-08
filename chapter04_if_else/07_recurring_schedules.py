day_of_month = 14

if day_of_month % 7 == 0:
    print("Weekly team meeting day!")  # This will run! (14 % 7 = 0)
elif day_of_month % 30 == 0:
    print("Monthly report is due!")