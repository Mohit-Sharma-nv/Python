# list, set, dictionary

my_list = [char for char in "helllo"]
my_list2 = [num for num in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
# keep only even num
my_list4 = [num**2 for num in range(0,100) if num%2 ==0]

print(my_list4)

simple_dict ={
    'a':1,
    'b':2
}

my_dict = {key:value**2 for key,value in simple_dict.items()}

your_dict = {num:num*2 for num in [1,2,3,4,5]}

print(your_dict)