# args and kwargs

def sup_fun(*args,**kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(sup_fun(1,2,3,4,5,6, num1 = 10, num = 20))
# Rule: paramter , *args , default par, **kwargs