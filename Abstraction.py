from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts using a key or push button.")


class Bike(Vehicle):

    def start(self):
        print("Bike starts using a self-start button or kick.")


car = Car()
bike = Bike()

car.start()
bike.start()


# Here ABC stands for Abstract Base Class and abc stands for a module (a Python file that contains pre-written code.)
# ABC is a special kind of class where Python knows this class can contain abstract methods.