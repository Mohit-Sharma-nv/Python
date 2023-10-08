# To define/create a function def keyword is used

def say_hello():
    print('hello buddy ')

say_hello()

# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# for items in picture:
#     print(items)

def show_GUI():
    for image in picture:
        for pixel in image:
            if pixel == 1:
                print("*", end="")
            else:
                print(" ", end="")

        print("")

show_GUI()
print(show_GUI)
print(say_hello) # show the location where its stores

# parameter
# default paramter
def hi(name ='Mohit Sharma', emoji='😍'):
    print(f"Hi, {name} have a good day {emoji}")

# Positional argument
hi('Mohit','😊')
hi('Sharma Ji','😊')

# Keyword Argument
hi(emoji='😊', name="What")



