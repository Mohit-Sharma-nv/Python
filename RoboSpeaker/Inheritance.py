# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent
# class is the class being inherited from, also called base class. Child class is the class that inherits from
# another class, also called derived class.

class User():

    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power {self.power}")

class Anchor(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"Attacking with Arrows: Arrows left -  {self.arrows}")

wizard1 = Wizard("Robin", 40)

wizard1.attack()
anchor1 = Anchor("Firly", 30)

anchor1.attack()

print(isinstance(anchor1, Anchor))
print(isinstance(anchor1, object))

