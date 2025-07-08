# Regular string - backslashes can cause issues
file_path = "C:\new_folder\tasks"  # The \n and \t get treated as newline and tab!

# Raw string - backslashes are treated as literal characters
file_path = r"C:\new_folder\tasks"  # This works perfectly!
print(file_path)

# Another example where raw strings are helpful
regex_pattern = r"\d+\.\d+"  # Looking for numbers like 123.45
print("Regex pattern:", regex_pattern)