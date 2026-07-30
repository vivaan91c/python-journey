# You're building the backend of a REST API server. 
# Every endpoint needs logging, authentication, timing, and formatting.
# Instead of repeating this logic in every function, you'll build a decorator toolkit — 
# one decorator for each job — and stack them on your API endpoints.


# 1) Pass a handler as an object

# Define a function "handle_request" that prints "Handling request...".
# Store it in a variable "handler". Then define "run_handler(fn)" that calls fn(). 
# Call run_handler(handler).

def handle_request():
    print("Handling request...")

handler = handle_request

def run_handler(func):
    func()

run_handler(handler)


# Here, there are no parentheses after handle_request.
# Therefore, Python does not execute the function. Instead, it stores a reference to the function inside handler.


# 2) Build a response formatter factory

# Define "make_formatter(prefix)" that defines and returns an inner function "format_response(data)"
# which returns prefix + data. Create a "json_format" formatter with prefix "JSON: " and test it.

def make_formatter(prefix):
    def format_response(data):
        return prefix + data
    return format_response

json_format = make_formatter("JSON: ")
print(json_format('{"name": "Vivaan"}'))


# 3) Build a logging decorator

# Create a "logger" decorator that prints "[LOG] Calling: function_name" before the function runs and "[LOG] Done" after. 
# Apply it to "get_users()" that prints "Fetching users...".

def logger(func):
    def wrapper():
        print("[LOG] Calling:", func.__name__)
        func()
        print("[LOG] Done")
    return wrapper

@logger
def get_users():
    print("Fetching users...")

get_users()


# 4) Make logger work with any endpoint

# Update your logger decorator to use *args and **kwargs so it works with functions that take arguments.
# Apply it to "get_user_by_id(user_id)" that prints "Fetching user: [id]". Call it with id=42.


def logger(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Calling:", func.__name__)
        func(*args, **kwargs)
        print("[LOG] Done")
    return wrapper

@logger
def get_user_by_id(user_id):
    print("Fetching user:", user_id)

get_user_by_id(42)


# 5) Time every API response

# Build a "timer" decorator using time.time() that prints how long each endpoint took to respond.
# Apply it to "process_order(order_id)" that prints "Processing order: [id]".

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")   # .4f controls how the decimal number is displayed.
        return result
    return wrapper

@timer
def process_order(order_id):
    print("Processing order:", order_id)

process_order(101)


# 6) Stack logger + timer on one endpoint

# Stack BOTH @logger and @timer on "get_analytics()" that prints "Loading analytics data...".
# Both decorators should fire — logger adds [LOG] messages, timer adds the timing.

def logger(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Calling:", func.__name__)
        func(*args, **kwargs)
        print("[LOG] Done")
    return wrapper

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")   
        return result
    return wrapper

@logger
@timer
def get_analytics():
    print("loading analytics data")

get_analytics()


# 7) Protect private endpoints with @login_required

# The final boss. Define a "login_required" decorator. Then stack THREE decorators 
# — @login_required, @logger, @timer — on "delete_account(user_id)". 
# Test with is_logged_in = True then False.


import time
is_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper

def logger(func):
    def wrapper(*args, **kwargs):
        print("[LOG] Calling:", func.__name__)
        result = func(*args, **kwargs)
        print("[LOG] Done")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper

@login_required
@logger
@timer
def delete_account(user_id):
    print("Deleting account:", user_id)

delete_account(7)


