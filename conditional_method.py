# Conditionals Practice
# Topics: if, if/else, if/elif/else,
#         and/or/not, in/not in,
#         nested if, if in loops, ternary


# 1.example on - and / not 

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician and not is_expert:
    print("At least you are getting there")

elif not is_magician:
    print("You need magic powers")


# 2.example on Nested if / if-elif-else

is_active = True
tier = "Gold"

if is_active:
    if tier == "Platinum":
        print("Withdrawal limit: ₹1,00,000")
    elif tier == "Gold":
        print("Withdrawal limit: ₹50,000")
    else:
        print("Withdrawal limit: ₹20,000")
else:
    print("Account inactive")


# 3.example on if in loops

employees = [
    {"name": "Kavya", "salary": 75000},
    {"name": "Arjun", "salary": 45000},
    {"name": "Sneha", "salary": 90000},
    {"name": "Mehul", "salary": 55000}
]

for employee in employees:
    if employee["salary"] >= 60000:
        name = employee["name"] + " senior"
    else:
        name = employee["name"] + " junior"

    print(name)


# 4.example on Ternary operator

qty = 15

status = "In Stock" if qty > 0 else "Out of Stock"

print(status)
