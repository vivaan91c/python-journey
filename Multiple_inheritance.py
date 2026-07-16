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

    def check_arrow(self):
        print(f"attacking with arrows: arrows left - {self.num_arrows} ")

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hb1 = HybridBorg("Aryan", 50, 100 )
print(hb1.sign_in())
print(hb1.attack())
print(hb1.check_arrow())
        
# Wizard1 = Wizard("vivaan", 50)
# Archer1 = Archer("Robin", 70)
# Wizard1.attack()
# Archer1.attack()