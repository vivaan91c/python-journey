# A decorator is a function that wraps another function 
# to add extra behaviour — without changing the original function's code.


# 1) fn as object

# Define a function "shout" that prints "HEY!". Store it in a variable "speak".
# Then define another function "execute(func)" that calls func(). Call execute() passing speak.

def shout():
    print("HEY!")

speak = shout

def execute(func):
    func()

execute(speak)


# 2) fn inside fn

# Define a function "make_multiplier(n)" that defines and returns an inner function "multiply(x)" that returns x * n.
# Create a "double" function using make_multiplier(2) and test it.

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(5))  
print(double(8))   


# 3) basic decorator

# Create a decorator "add_border" that prints "======" before and after any function it decorates. 
# Apply it to a function "show_title" that prints "Sales Report"

def add_border(func):  # here func refers to show_title
    def wrapper():
        print("======")
        func()         # here func refers to show_title
        print("======")
    return wrapper

@add_border
def show_title():
    print("Sales Report")

show_title()


# 4) decorator with args

# Create a decorator "uppercase_result" that converts the return value of a function to uppercase.
# Apply it to "get_city()" that returns "mumbai". Print the result.

def uppercase_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase_result
def get_city():
    return "mumbai"

print(get_city())  


# 5) timing decorator

# Create a timer decorator and apply it to a function "calculate_squares"
# that uses a list comprehension to get squares of numbers 1–1000. Print how long it took.


import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@timer
def calculate_squares():
    return [n**2 for n in range(1, 1001)]

calculate_squares()


# 6) stacking decorators

# Create two decorators: 1. "bold" — wraps output with **text** 
# 2. "italic" — wraps output with _text_ Stack both on "get_title()" that returns "Python". 
# Print the result.

def bold(func):
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return f"_{func(*args, **kwargs)}_"
    return wrapper


@bold
@italic
def get_title():
    return "Python"


print(get_title())


# 7) @login_required

# Build a login_required decorator. It checks if "is_logged_in" is True.
# If yes, run the function. If no, print "Access denied. Please log in."
# Apply it to "view_dashboard()" and test both cases.

is_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper

@login_required
def view_dashboard(username, section):
    print(f"Welcome {username}!")
    print(f"You are viewing the {section} section.")


view_dashboard("Vivaan", section="Profile")