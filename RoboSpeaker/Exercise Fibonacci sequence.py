def fib(number):
    num1 = 0
    num2 = 1
    next_num = num1
    count = 1

    while count<=number:
        print(next_num,end=" ")
        count +=1
        num1,num2 = num2 ,next_num
        next_num = num1 + num2

    print()

# fib(21)


# Fibonacci using generator

def fib2(num):
    a = 0
    b = 1
    next = b

    for i in range(num):
        yield a
        a, b = b, next
        next = a + b


for x in fib2(20):
    print(x, end=" ")