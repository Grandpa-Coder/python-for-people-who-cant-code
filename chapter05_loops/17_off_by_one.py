# Wrong: This accidentally misses the last item
my_list = ["apple", "banana", "cherry"]
for i in range(len(my_list) - 1):  # Oops! This stops one short
    print(my_list[i])

# Right: This gets all items
for i in range(len(my_list)):
    print(my_list[i])

# Even better: Let Python handle the details
for item in my_list:
    print(item)  # Clean and simple!