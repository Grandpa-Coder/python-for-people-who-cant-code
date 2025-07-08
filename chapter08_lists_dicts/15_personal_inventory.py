# Create your inventory
my_books = [
    {"title": "Python for Practical People", "author": "Someone Smart", "pages": 300, "read": True},
    {"title": "The Art of Not Being Overwhelmed", "author": "A Wise Person", "pages": 250, "read": False},
    {"title": "Coffee: A Love Story", "author": "A Kindred Spirit", "pages": 180, "read": True}
]

# Print your collection
print("My Book Collection:")
for book in my_books:
    status = "✓ Read" if book["read"] else "⏳ To Read"
    print(f"  '{book['title']}' by {book['author']} ({book['pages']} pages) - {status}")

# Add a new book
new_book = {
    "title": "Data Structures for Normal People", 
    "author": "Another Smart Person", 
    "pages": 275, 
    "read": False
}
my_books.append(new_book)

print(f"\nAdded new book! Collection now has {len(my_books)} books.")