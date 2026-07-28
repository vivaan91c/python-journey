# Build a tax calculator with lambda

# 1) Create a lambda called "add_tax" that takes a revenue value and returns it with 18% GST added. 
# Test it with revenue = 50000.

add_tax = lambda r: r + r * 0.18
print(add_tax(50000))  


# 2) Apply tax to all revenues

# Use map() with your add_tax lambda to apply 18% GST to every revenue in the list.
# Store in "revenues_with_tax" and print.


revenues = [45000, 82000, 31000, 97000, 56000, 23000, 74000]
add_tax = lambda r: r + r * 0.18
revenues_with_tax = list(map(add_tax, revenues))
print(revenues_with_tax)


# 3) Find top performers

# Filter the revenues list to keep only the high performers 
# ie those with revenue above 50000. Store in "top_revenues" and print.


revenues = [45000, 82000, 31000, 97000, 56000, 23000, 74000]
top_revenues = list(filter(lambda r : r > 50000, revenues))
print(top_revenues)


# 4) Pair employees with their revenues

# Use zip() to pair each employee name with their revenue.
# Loop through and print each pair as "name: ₹revenue".

employee = ["Niya", "Arjun", "Sneha", "Mehul", "Pooja", "Karan", "Divya"]
revenue  = [45000, 82000, 31000, 97000, 56000, 23000, 74000]

for employee, revenue in zip(employee, revenue):
    print(f"{employee} has {revenue}")



# 5) Calculate total company revenue

# Use reduce() to sum all revenues into a single total. Store in "total_revenue" and print.

from functools import reduce
revenues = [45000, 82000, 31000, 97000, 56000, 23000, 74000]

total_revenue = reduce(lambda a, b: a + b, revenues)
print(total_revenue)  


# 6) Generate a performance report

# Use a list comprehension to build a report list.
# For each revenue, create a string "₹revenue — HIGH" if revenue > 60000, or "₹revenue — LOW" otherwise.
# Store in "report" and print.


revenues = [45000, 82000, 31000, 97000, 56000, 23000, 74000]
report = [
    f"₹{r} — {'HIGH' if r > 60000 else 'LOW'}"
    for r in revenues
]
print(report)


# 7) Build the employee revenue lookup

# The final boss. 
# Use a dict comprehension with zip() to create a dictionary mapping each employee name to their revenue. 
# Store in "emp_revenue" and print.

employee = ["Niya", "Arjun", "Sneha", "Mehul", "Pooja", "Karan", "Divya"]
revenue  = [45000, 82000, 31000, 97000, 56000, 23000, 74000]

employee_revenue = {employee: revenue for employee, revenue in zip(employee, revenues)}
print(employee_revenue)


# note: dictionary comprehension is similar to zip function