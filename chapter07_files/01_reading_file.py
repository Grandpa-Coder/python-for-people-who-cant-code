with open("clients.txt", "r") as client_file:
    all_clients_text = client_file.read()

print("Here are all my clients:")
print(all_clients_text)