# Determine the type of an object at Run time

# dir keyword is used

class User():

    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power


wizard1 = Wizard("Ram",20)
print(dir(wizard1))