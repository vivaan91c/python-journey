# For loop Methods Practice
# Topics: using list, dictionary, enumerate function, continue and break

players = ["Virat", "Rohit", "Gill"]

# for list
for player in players:
    print(player)

# for range
for number in range(1, 6):
    print(number)

# for dictionary
student = {
    "name": "Vivaan",
    "age": 19,
    "city": "Mumbai"
}

for key, value in student.items():
    print(key, value)

# for enumerate
for index, player in enumerate(players):
    print(index, player)

# continue
for number in range(1, 6):

    if number == 3:
        continue

    print(number)

# break
for number in range(1, 11):

    if number == 6:
        break

    print(number)