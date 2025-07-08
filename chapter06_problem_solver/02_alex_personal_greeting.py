def alex_personal_greeting(client_name, time_of_day):
    print(f"Good {time_of_day}, {client_name}!")
    print("Thank you for choosing Alex's Business Solutions.")
    if time_of_day == "morning":
        print("I hope you're having a great start to your day!")
    elif time_of_day == "afternoon":
        print("I hope your day is going smoothly!")
    else:
        print("I hope you're winding down nicely!")
    print("(Coffee not included, but highly recommended)")

# Alex uses it with different clients and times
alex_personal_greeting("Sarah's Bakery", "morning")
alex_personal_greeting("Metro Hardware", "afternoon")  
alex_personal_greeting("Johnson Family Dental", "evening")