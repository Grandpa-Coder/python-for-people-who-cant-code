responses = []
print("Customer Satisfaction Survey")
print("Rate us 1-5 (or type 'done' to finish)")

while True:  # This creates an infinite loop on purpose...
    rating = input("Your rating: ")
    
    if rating.lower() == 'done':  # ...but we have a secret escape hatch!
        break
    
    try:  # This is like wearing a safety helmet for your code
        rating_number = int(rating)
        if 1 <= rating_number <= 5:
            responses.append(rating_number)
            print("Thank you for your feedback!")
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:  # If they type something that's not a number
        print("Please enter a valid number or 'done'.")

# Calculate average (if we got any responses)
if responses:
    average = sum(responses) / len(responses)
    print(f"\nSurvey complete! Average rating: {average:.1f}")
else:
    print("No responses collected. Maybe try offering cookies next time!")