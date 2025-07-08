file_name = "client_list.txt"

print(f"Reading clients from: {file_name}")
print("-" * 40)

with open(file_name, "r") as clients_file:
    for client_name in clients_file:
        cleaned_name = client_name.strip()  # Remove any extra spaces or invisible characters
        if cleaned_name:  # Only process non-empty names
            print(f"Preparing personalized email for: {cleaned_name}")
            print(f"  Subject: Special offer just for you, {cleaned_name}!")

print("\nEmail preparation complete! Time for coffee.")