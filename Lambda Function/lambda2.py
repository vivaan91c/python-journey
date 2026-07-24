# Create a lambda called "get_discount" that takes a price and returns the price after 20% discount.
# Test it with price = 5000.


get_discount = lambda price: price - (price * 0.20)
print(get_discount(5000))  