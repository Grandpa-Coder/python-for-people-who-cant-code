file_name = "product_codes.txt"  # Ah, there's the correct name!

with open(file_name, "r") as codes_file:
    for code in codes_file:
        print(f"Processing code: {code.strip()}")