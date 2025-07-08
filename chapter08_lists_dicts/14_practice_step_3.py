family = [
    {"name": "Alex", "age": 45, "hobby": "Photography"},
    {"name": "Sam", "age": 12, "hobby": "Soccer"},
    {"name": "Robin", "age": 42, "hobby": "Gardening"}
]

print("Family members:")
for person in family:
    print(f"  {person['name']} enjoys {person['hobby']}")