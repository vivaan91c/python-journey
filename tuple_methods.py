# Tuples

# Topics: tuple basics, indexing, slicing, len(),
#         count(), index(), unpacking,
#         immutability,
#         add(), discard(), remove(), pop(),
#         in operator,

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Access using index
print(weekdays[0])

# Access using negative index
print(weekdays[-1])

# Tuple slicing
print(weekdays[1:4])

# Length of tuple
print(len(weekdays))

# Count method
numbers = (1, 2, 3, 2, 4, 2, 5)
print(numbers.count(2))

# Index method
print(weekdays.index("Wed"))

# Membership operator
print("Mon" in weekdays)
print("Sun" in weekdays)

# Tuple unpacking
day1, day2, day3, day4, day5 = weekdays

print(day1)
print(day2)
print(day3)
print(day4)
print(day5)

# Tuple immutability workaround
temp = list(weekdays)

temp.append("Saturday")
temp.append("Sunday")

weekdays = tuple(temp)

print(weekdays)


