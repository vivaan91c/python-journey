def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))


# filter function allows us to filter things for us

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,[1,2,3])))