# You're building the backend of an e-commerce platform.
# You need functions to greet customers, calculate prices, apply discounts, analyse orders, categorise products
# process a full order list, and compose it all together into one final bill 

# 1) Greet the customer

def show_banner():
    print("Welcome to ShopEasy — India's #1 Store!")

show_banner()


# 2) Display product details

def show_product(name, price, brand):
   print(f"The name of product is {name}, of brand {brand}, with the price tag of {price}")

show_product("Laptop", 75000, "Dell")
show_product("Mouse", 1200, "Logitech")


# 3) Calculate Subtotal using return
 
def get_subtotal(price, qty):
    return price * qty

result = get_subtotal(75000, 2)
print(result) 


# 4) Apply discount with default

def after_discount(price, discount = 5):
    return price - (price * discount / 100)

item1 = after_discount(150000)
item2 = after_discount(150000, 15)

print(item1)
print(item2)


# 5) Analyse the order

def analyse_order(prices):
    return min(prices), max(prices), sum(prices)

prices = [75000, 1200, 3500, 8000]

cheapest, priciest, total = analyse_order(prices)
print(cheapest)  
print(priciest)  
print(total)


# 6) Categorise each product by price

def get_category(price):
    if price < 2000:
        return "Budget"
    elif price <= 50000:
        return "Mid-range"
    else:
        return "Premium"

print(get_category(1200))  
print(get_category(8000))   
print(get_category(75000))


# 7) Process every item in the cart

cart = [
    {"name": "Laptop",     "price": 75000},
    {"name": "Headphones", "price": 8000},
    {"name": "Cable",      "price": 500},
    {"name": "Keyboard",   "price": 3500}
]

def get_category(price):
    if price < 2000:
        return "Budget"
    elif price <= 50000:
        return "Mid-range"
    else:
        return "Premium"


for item in cart:
    print(f"The product name is {item['name']} which belongs to the category {get_category(item['price'])}")


# 8) Build the final bill

