import datetime

# Get today's date automatically (because who remembers what day it is?)
today = datetime.date.today()
new_log_entry = f"\n[{today}] - Customer called asking if we sell invisible products. Explained that we don't, but appreciated their optimism."

with open("support_log.txt", "a") as log_file:
    log_file.write(new_log_entry)

print("New log entry added to support_log.txt")
print("(Your support log is getting more interesting by the day!)")