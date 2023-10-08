# Higher order function HOC
#  its a function that accept the another function in its paramter or return a function

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func

a = greet(greet2)
print(a)

# Decorator
def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print("*******")
        func(*args,**kwargs)
        print("*******")
    return wrap_func

@my_decorator
def hello():
    print("heellllo")

@my_decorator
def bye():
    print("see ya later")

hello()
bye()

@my_decorator
def hi(gretting):
    print(gretting)

hi("Hi, How are you!!")

@my_decorator
def why(greet, emoji):
    print(greet, emoji)

why("hello",":)")