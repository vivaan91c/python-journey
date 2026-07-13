class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner            # Public variable ie Outside class Can access directly
        self.__balance = balance      # Private variable ie Outside class Cannot access directly

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.__balance)


account = BankAccount("Vivaan", 10000)

account.show_balance()

account.deposit(5000)

account.withdraw(3000)

account.show_balance()


# Encapsulation means:

# Keeping data (variables) and the methods that work on that data together inside one class,
# while preventing direct access to important data. ie account balance

# In this example:

# Data = owner, __balance
# Methods = deposit(), withdraw(), show_balance()

# Everything is wrapped inside the BankAccount class.