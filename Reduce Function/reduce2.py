# Use reduce() to find the sum all numbers
from functools import reduce

nums = [1, 2, 3, 4, 5]

# sum all numbers
total = reduce(lambda a, b: a + b, nums)
print(total)  # 15

# how it works step by step:
# (1+2)=3 → (3+3)=6 → (6+4)=10 → (10+5)=15


# Use reduce() to find the product (multiplication) of all numbers in the list. Import reduce first.

from functools import reduce
nums = [2, 3, 4, 5]
result = reduce(lambda a, b: a * b, nums)
print(result)  