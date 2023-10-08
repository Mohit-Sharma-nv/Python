# counter

my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for items in my_list:
    sum = sum + items

print(len(my_list))
print(sum)

for i, char in enumerate("helloooo"):
    print(i,char)

for i,char in enumerate(list(range(100))):
    print(i,char)

    if (char == 50):
        print(f"Index of 50 is {i}")


