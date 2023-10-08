from functools import reduce
def multiple_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list

print(multiple_by2([1,2,3]))

# map , filter, zip and reduce

# map
def multiple_by3(item):
    return item*3

print(list(map(multiple_by3,[1,2,3])))

# Filter
def only_odd(item):
    return item %2 != 0

print(list(filter(only_odd,[1,2,3])))

# Zip

list1 = [1,2,3]
list2 = [20,30,40]

print(list(zip(list1,list2)))

# Reduce
def accumulator(acc, item):
    print(acc,item)
    return acc + item

print(reduce(accumulator,list1,0))

# lambda Expersion
print(list(map(lambda item: item*2, [1,2,3,4])))