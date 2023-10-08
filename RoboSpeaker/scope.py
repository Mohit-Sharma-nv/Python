# Scope - What variable I have access to?

if True:
    x = 50

def some_fun():
    total = 10

print(x)
# print(total)
# NameError: name 'total' is not defined

a = 1
def parent():
    def confussion():
        a = 5
        return sum
    return confussion()

print(a)
print(parent())

# Rules
# 1 - start with local
# 2 - parent local
# 3- global?
# 4- build in python function

# accesing the global variable

total = 0

def count():
    global total
    total +=1
    return total

count()
count()
print(count())

def outer():
    x ="local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: ", x)

    inner()
    print("outer: ", x)

outer()