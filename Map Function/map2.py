# You have a list of prices in USD. 
# Use map() with a lambda to convert all of them to INR (multiply by 83).
# Store in "prices_inr" and print.


prices_usd = [10, 25, 50, 100, 200]
prices_inr = list(map(lambda p: p * 83, prices_usd))
print(prices_inr)  