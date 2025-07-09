# Project 2: The Personal Email Butler
# (Way classier than a regular butler - this one works with emails!)

print("*** Starting Personal Email Butler ***")
print("(No tuxedo required, but feel free to wear one for the full experience)")

# Our settings (like programming the butler's instructions)
recipient_file_name = "recipients.txt"
subject = "Your Weekly Marketing Update from Alex"

# This is our email template - notice the {name} placeholder
message_template = """
Dear {name},

Hope your week is going better than a cat video going viral!

Here's your weekly update from Alex's Marketing Consultancy. This week, we've been busy helping businesses like yours discover the magic of digital marketing (and occasionally debugging Python scripts, but that's another story).

Key highlights:
* We've helped 3 new clients boost their online presence
* Our latest blog post about social media myths got shared 247 times
* We successfully automated our invoice processing (thanks, Python!)

Got questions? Just hit reply - I actually read my emails (revolutionary concept, I know).

Stay awesome,
Alex

P.S. - If you're wondering why this email sounds more cheerful than usual, it's because I'm no longer spending Monday mornings with a calculator!
"""

print(f">>> Using email template with subject: '{subject}'")
print("Let's personalize some emails!")

try:
    # Open our client list
    with open(recipient_file_name, "r") as file:
        email_count = 0
        
        for line in file:
            cleaned_line = line.strip()
            
            # Skip empty lines (because empty lines are boring)
            if cleaned_line:
                # Split the line into name and email
                parts = cleaned_line.split(',')
                
                if len(parts) == 2:
                    client_name = parts[0].strip()
                    client_email = parts[1].strip()
                    
                    # Create the personalized message (the magic moment!)
                    personalized_message = message_template.format(name=client_name)
                    
                    email_count += 1
                    
                    # Show what the email would look like
                    print(f"\n>>> EMAIL #{email_count} - SIMULATION MODE")
                    print("=" * 60)
                    print(f"To: {client_email}")
                    print(f"Subject: {subject}")
                    print(f"Message:")
                    print(personalized_message)
                    print("=" * 60)
                    print(f"*** Email for {client_name} ready to send! ***")
                    
                else:
                    print(f"??? Hmm, this line looks weird: '{cleaned_line}'")
                    print("Expected format: 'Name,email@example.com'")

    print(f"\n*** Email Butler Mission Complete! ***")
    print(f">>> Generated {email_count} personalized emails")
    print("*** Ready to impress your clients with personalized communication! ***")

except FileNotFoundError:
    print(f"Oops! Couldn't find '{recipient_file_name}'")
    print("Make sure your client list file is in the same folder as this script.")
    print("(It's like preparing a dinner party but forgetting to make the guest list!)")
    
except Exception as e:
    print(f"!!! Something unexpected happened: {e}")
    print("Don't worry - even the best butlers have off days!")