# Square
my_list = [5, 4, 3]

new_list = list(map(lambda item: item*item, my_list))
print(new_list)

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])
print(a)

# over here "x" means the list
# and x[1] means traversing through index 1 of each tuple and sorting them based on the index 1