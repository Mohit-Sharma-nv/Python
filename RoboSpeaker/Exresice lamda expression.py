# Lambda expression that square the list

my_list = [5,4,3]
print(list(map(lambda item: item**2, my_list)))

# List sorting

a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x: x[1])
print(a)