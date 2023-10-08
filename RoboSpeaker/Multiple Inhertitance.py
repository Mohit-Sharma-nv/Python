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

    def run(self):
        print("ran really fast")

    def attack(self):
        print(f"Attacking with Arrows: Arrows left -  {self.arrows}")

class HybridBorg(Wizard,Anchor):
    def __init__(self,name,power,arrows):
        Anchor.__init__(self,name,arrows)
        Wizard.__init__(self,name,power)

hb1 = HybridBorg("Ram",100, 302)
print(hb1.sign_in())
print(hb1.attack())
print(hb1.run())