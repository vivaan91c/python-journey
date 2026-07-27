# Dictionary comprehension builds a dict in one line using {key: value for item in iterable}.
# Set comprehension builds a set in one line using {expression for item in iterable} — automatically removes duplicates.

# Dict comprehension
names = ["Niya", "Arjun", "Sneha"]
lengths = {name: len(name) for name in names}
print(lengths)
# {"Niya": 4, "Arjun": 5, "Sneha": 5}

# Set comprehension
nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n**2 for n in nums}
print(unique_squares)
# {1, 4, 9, 16}

# -------------------------------------------------------------------------------------------------------

# 1. Create a dict comprehension mapping each product to its price squared (for a weird pricing algorithm).

products = {"Laptop": 75000, "Mouse": 1200, "Keyboard": 3500, "Monitor": 22000}
squared_prices = {name: price**2 for name, price in products.items()}
print(squared_prices)

# 2. Create a set comprehension of unique first letters from the product names.

products = {"Laptop": 75000, "Mouse": 1200, "Keyboard": 3500, "Monitor": 22000}
first_letters = {name[0] for name in products}
print(first_letters) 