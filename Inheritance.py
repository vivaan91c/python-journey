class User():
    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows} ")
        
Wizard1 = Wizard("vivaan", 50)
Archer1 = Archer("Robin", 70)
Wizard1.attack()
Archer1.attack()