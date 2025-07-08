day = "Monday"
time_of_day = 15  # 3 PM in 24-hour format

if day == "Monday":
    print("Manic Monday special: Extra shot for free!")
elif time_of_day >= 15:
    print("Afternoon pick-me-up: Try our pastries!")
elif time_of_day % 2 == 0:
    print("Even hour special: 10% off!")