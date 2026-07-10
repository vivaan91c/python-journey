# 1) USING return WITH FUNCTIONS

def calculate_total(price, qty):
    return price * qty


result = calculate_total(500, 4)

print(result)


# 2) USING DEFAULT PARAMETERS IN FUNCTION

def apply_discount(price, discount=0.1):
    return price * discount


old_discount = apply_discount(5000, 0.1)
print(old_discount)

new_discount = apply_discount(5000, 0.2)
print(new_discount)


# 3) RETURNING MULTIPLE VALUES FROM A FUNCTION

def analyse_marks(marks):
    return min(marks), max(marks), sum(marks) / len(marks)


low, high, avg = analyse_marks([88, 45, 92, 67, 78])

print(low)    
print(high)   
print(avg)   


# 4) DIFFERENCE BETWEEN print() AND retur


# Using print()
# Result is displayed, but nothing is returned

def add_with_print(a, b):
    print(a + b)


add_with_print(3, 4)          # Displays 7

result = add_with_print(3, 4)

print(result)                 # Displays None



# Using return
# Result comes back and can be reused

def add_with_return(a, b):
    return a + b


result = add_with_return(3, 4)

print(result)                 # 7
print(result * 2)             # 14


# 5) BMI CATEGORISATION USING A FUNCTION

def categorise_bmi(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


print(categorise_bmi(22.4))   