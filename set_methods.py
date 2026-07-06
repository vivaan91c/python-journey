# Set Practice
# Topics: remove, add, union, intersection.


registrations = ["Amit", "Sara", "Amit", "Raj", "Sara", "Amit"]

# Remove duplicates
unique_students = set(registrations)

# Add a student
unique_students.add("Vivaan")

# Safe removal
unique_students.discard("Rahul")

# Membership checking
has_sara = "Sara" in unique_students
has_rahul = "Rahul" in unique_students

# Another set
new_registrations = {"Vivaan", "Karan", "Raj"}

# Union
all_students = unique_students.union(new_registrations)

# Intersection
common_students = unique_students.intersection(new_registrations)

print(unique_students)

print(has_sara)
print(has_rahul)

print(all_students)

print(common_students)