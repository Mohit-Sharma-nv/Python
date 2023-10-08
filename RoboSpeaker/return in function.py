def sum(num1,num2):

    def another_fun(num1 , num2):
        return  num1 + num2

    return another_fun
# print(sum(10,15))
total = sum(10,15)
print(total(20,55))
