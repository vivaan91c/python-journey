# While Practice
# Topics: Basic condition, break, nested while loop

count = 1

while count <= 5:
    print(count)
    count += 1

# while condition

age = 16

while age < 18:
    print("Not eligible")
    age += 1

print("Eligible")

# while break

number = 1

while number <= 10:

    if number == 6:
        break

    print(number)

    number += 1

# nested loops

row = 1

while row <= 3:

    column = 1

    while column <= 3:
        print(row, column)
        column += 1

    row += 1