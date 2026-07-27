# A list comprehension builds a new list in one line using a compact syntax.

# Loop way
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# List comprehension — same result
squares = [n ** 2 for n in range(1, 6)]
print(squares) 

# With filter condition
evens = [n for n in range(1, 11) if n % 2 == 0]
print(evens)  


# Use a list comprehension to create a list of all numbers from 1 to 20 that are divisible by 3.
# Store in "div_by_3" and print.

div_by_3 = [n for n in range(1, 21) if n % 3 == 0]
print(div_by_3)  # [3, 6, 9, 12, 15, 18]