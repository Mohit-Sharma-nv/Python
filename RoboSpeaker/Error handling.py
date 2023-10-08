# Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        0/age
        print(age)
    except ValueError:
        print("Please enter the number")
    except ZeroDivisionError:
        print("Please enter the number greater than zero")
    else:
        print("Thank you!!")
        break





def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter the number and there is {err}  ")



print(sum("1",3))