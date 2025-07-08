file_name = "prod_codes.txt"  # Oops! The actual file is called "product_codes.txt"

with open(file_name, "r") as codes_file:
    for code in codes_file:
        print(f"Processing code: {code.strip()}")