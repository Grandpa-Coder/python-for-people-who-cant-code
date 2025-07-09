# Project 1: The Invoice Whisperer
# (Because we're going to whisper sweet nothings to our invoices)

print("*** Starting Invoice Summary Magic ***")
print("(Don't worry, no actual magic required - just Python!)")

# This is our money bucket - starts empty, gets fuller as we go
total_sales = 0.0

# The name of our invoice file (like a label on a filing cabinet)
invoice_file_name = "invoices.txt"

# Here's where we do the smart stuff
try:
    # Open the file (like opening a book to read)
    with open(invoice_file_name, "r") as file:
        print(f">>> Successfully opened {invoice_file_name}")
        print("Reading invoices one by one...")
        
        # Read each line (like reading each page of the book)
        for line in file:
            try:
                # Clean up the line (remove extra spaces and weird characters)
                cleaned_line = line.strip()
                
                # If the line isn't empty (ignore blank lines)
                if cleaned_line:
                    # Turn the text into a number (the magical transformation!)
                    amount = float(cleaned_line)
                    total_sales += amount
                    print(f">>> Added ${amount:.2f} to the total")
                    
            except ValueError:
                # Sometimes we find weird stuff in files - let's handle it gracefully
                print(f"??? Hmm, '{line.strip()}' doesn't look like a number. Skipping it!")

    # The grand finale!
    print("\n" + "="*50)
    print(f"*** DRUM ROLL PLEASE... ***")
    print(f"*** Total Sales: ${total_sales:.2f} ***")
    print("*** Invoice summary complete! Time for a victory lap! ***")
    print("="*50)

except FileNotFoundError:
    print(f"Oops! Couldn't find the file '{invoice_file_name}'")
    print("Make sure it's in the same folder as this script.")
    print("(It's like looking for your car keys - check the obvious place first!)")
    
except Exception as e:
    print(f"!!! Something unexpected happened: {e}")
    print("Don't panic! This is totally normal when learning.")