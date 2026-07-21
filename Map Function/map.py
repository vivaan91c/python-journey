def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3]))


# map function allows us to simplify the code

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))


# both of these code give the same output , except using map function our code gets simplified and smaller.