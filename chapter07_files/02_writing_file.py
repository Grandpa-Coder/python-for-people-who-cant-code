report_data = "Daily Sales Report: June 18, 2025\n"
report_data += "Total sales: $1,250.75\n"
report_data += "New customers: 5\n"
report_data += "Best selling item: Coffee mugs (because everyone needs more coffee)"

with open("sales_report.txt", "w") as report_file:
    report_file.write(report_data)

print("Sales report written to sales_report.txt")
print("(Check the same folder as your Python script - there should be a new file there!)")