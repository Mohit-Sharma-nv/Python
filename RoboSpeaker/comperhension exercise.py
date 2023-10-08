some_list = ['a','b','c','b','d','m','n','n']

# duplicate = {char for char in some_list if some_list.count(char) > 1}
duplicate = list(set([char for char in some_list if some_list.count(char)>1]))

print(duplicate)