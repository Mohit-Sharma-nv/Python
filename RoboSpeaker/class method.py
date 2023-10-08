# Class Method

class PlayerChr:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def run(self):
        return self

    @classmethod
    def addingthings(cls,num1,num2):
        return  cls("Teddy" ,num1 + num2)

    @staticmethod
    def addingthings2( num1, num2):
        return num1 + num2


player3 = PlayerChr.addingthings(1,2)
print(player3.name)

print(PlayerChr.addingthings2(20,10))

print(player3.run())
