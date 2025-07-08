invoice_number = 127
invoice_status = "pending"
days_past_due = 5

# Check invoice status and take action
if invoice_status == "overdue":
    print("Sending overdue reminder to client.")
elif invoice_status == "pending" and days_past_due > 0:
    print("Invoice is pending and past due. Sending a gentle reminder.")
elif invoice_status == "paid":
    print("Invoice paid. No action needed. *Happy dance*")
else:
    print("Invoice status unknown or no action required.")

# Batch processing check using modulo
if invoice_number % 25 == 0:
    print("Milestone reached! Time to review this quarter's invoices.")
elif invoice_number % 10 == 0:
    print("Processing batch of 10 invoices complete.")