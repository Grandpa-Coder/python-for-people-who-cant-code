hour = 8
day_of_week = 3  # Wednesday
task_count = 15

if hour < 9:
    print("Early bird! Perfect time to check emails.")  # This will run! (8 < 9)
elif hour == 12:
    print("Lunch time! Take a well-deserved break.")
elif task_count % 5 == 0:
    print("Milestone reached! You've completed 15 tasks.")
elif day_of_week == 5:  # Friday
    print("It's Friday! Almost weekend time.")