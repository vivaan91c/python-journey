# You have two lists — student names and their scores.
# Use zip() to pair them up and loop through printing "name: score" for each student.


names  = ["Jiya", "Arjun", "Sneha"]
scores = [88, 92, 76]

paired = list(zip(names, scores))
print(paired)

# Unpack in a loop
for name, score in zip(names, scores):
    print(f"{name} scored {score}")