# Dictionary Methods Practice
# Topics: access [], add/update [],
#         get(), remove()
#         values(), items()

student = {
    "name": "Vivaan",
    "age": 19,
    "course": "Python"
}

# Access value
print(student["name"])

# Safe access
print(student.get("city", "City not found"))

# Add new key
student["city"] = "Mumbai"

# Update existing key
student["age"] = 20

# Remove key
removed_course = student.pop("course")
print(removed_course)

# Get all keys as a list
keys_list = list(student.keys())
print(keys_list)

# Get all values as a list
values_list = list(student.values())
print(values_list)

# Get all items as a list
items_list = list(student.items())
print(items_list)

# Print final dictionary
print(student)