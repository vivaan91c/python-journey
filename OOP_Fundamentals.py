# class basics

class Student:
    pass

student1 = Student()
student2 = Student()
print(type(student1))


# __init__

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = Student("vivaan", "A")
print(student1.name)   
print(student1.grade)

# print(student1) -- this particular line shows us in the terminal the place at which our memory is stored


# 3) methods

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"Hi, I am {self.name} and my grade is {self.grade}")

student1 = Student("Aryan", "F")
student1.introduce()  


# 4) multiple objects

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"the brand of phone is {self.name} and price is {self.price}")

p1 = Product("apple", 60000)
p2 = Product("samsung", 50000)
p3 = Product("LG", 10000)

p1.show_details()
p2.show_details()
p3.show_details()


# 5) Intermediate OOP

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.owner, "— ₹", self.balance)

acc = BankAccount("vivaan", 10000)
acc.deposit(5000)
acc.show_balance()  


# 6) __str__

class Student():
    def __init__(self, name, grade):
     self.name = name
     self.grade = grade

    def __str__(self):
        return f"student: {self.name} | grade: {self.grade}"
      
student1 = Student("Vivaan", "A")
print(student1)


# 7) Inheritance [very important]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)   
        self.company = company
    
    def introduce(self):
        print(self.name, "| Age:", self.age, "| Company:", self.company)

e1 = Employee("Vivaan", 21, "Google")
e1.introduce()


#super().__init__(name, age) is used to call the constructor of the parent class, Person.
# so that we do not have to write self.name, self.age again.


# 8) objects in list

class Product():
    def __init__(self, name, price):
     self.name = name
     self.price = price

Products = [
Product("Heaphones", 3000),
Product("Phone", 50000),
Product("Laptop", 150000)
]

for self in Products:
 print(f"the name of product is {self.name} with the price tag of {self.price}")