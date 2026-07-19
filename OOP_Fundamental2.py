# 1) class basics

class Dog:          
    pass          

dog1 = Dog()     
dog2 = Dog()        

print(type(dog1))


# 2) __init__

class Dog:
    def __init__(self, name, breed):
        self.name = name    
        self.breed = breed  

dog1 = Dog("Bruno", "Labrador")
print(dog1.name)   
print(dog1.breed)  

# print(dog1)  -- this particular line shows us in the terminal the place at which our memory is stored


# 3) methods

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):           # method
        print(self.name, "says: Woof!")

dog1 = Dog("Bruno")
dog1.bark()   # Bruno says: Woof!


# 4) multiple objects

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand, "—", self.price)

p1 = Phone("Apple", 99000)
p2 = Phone("Samsung", 65000)
p3 = Phone("OnePlus", 45000)

p1.show()  # Apple — 99000
p2.show()  # Samsung — 65000


# 5) Intermediate OOP

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

car1 = Car("BMW", 0)
print(car1.speed)   # 0
car1.accelerate(60)
print(car1.speed)   # 60


# 6) __str__

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"{self.brand} — ₹{self.price}"

car1 = Car("BMW", 5000000)
print(car1)


# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):      # Dog inherits Animal
    def bark(self):
        print(self.name, "says Woof!")

d = Dog("Bruno")
d.eat()    # inherited from Animal
d.bark()   # Dog's own method


# 8) objects in list

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)

students = [
    Student("Aryan", [88, 92, 76]),
    Student("Pranjal", [65, 70, 80])
]

for self in students:
    print(f"the student {self.name} has an average of {self.average()}")