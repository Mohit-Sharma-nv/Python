# Set
my_set = {1,2,3,4,4,5,5,5,6,6,2}
my_set.add(100)
my_set.add(2)
print(my_set)
print(1 in my_set)
new_set = my_set.copy()
my_set.clear()
print(my_set)
print(new_set)

my_list = [1,2,3,4,5,5,5,5]
print(set(my_list))

print("*"*50)
# set methods
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
# print(set1.difference(set2))
# print(set1)
# print(set1.discard(3))
# print(set1)
# print(set1.difference_update(set2))
# print(set1)

# Intersection
# print(set1.intersection(set2))

print(set1.isdisjoint(set2))

# union
print(set1.union(set2))