class PlayerCharachter:
    # class object attribute
    membership = True
    def __init__(self, name , age):
        if (self.membership):
            self.name = name
            self.age = age

    def run(self):
        print("run")
        return done
    def shout(self):
        print(f"Hi, My name is {self.name}")
        return "Thank you "

    @classmethod
    def adding_thing(cls, num1, num2):
        return cls('Teddy', num1 + num2)

player1 = PlayerCharachter("John",21)
player2 = PlayerCharachter("rahul",40)
player2.attack = 50

print(player1.age)
print(player2.attack)
print(player1)
print(player2)
print(player1.membership)
print(player2.membership)

print(player1.name)

print(player1.shout())
print(player2.shout())

player3 = PlayerCharachter.adding_thing(2,3)
print(player3.name)




