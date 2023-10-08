# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent
# class is the class being inherited from, also called base class. Child class is the class that inherits from
# another class, also called derived class.

class User():
    def __init__(self,email):
        self.email = email


    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name, power,email):
        # User.__init__(self,email)
        # Another way to this
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power {self.power}")





wizard1 = Wizard("Robin", 40,"robin@gmail.com")
print(wizard1.sign_in())
print(wizard1.email)


