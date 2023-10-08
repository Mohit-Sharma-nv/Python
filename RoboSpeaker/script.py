# my_file = open("test.txt")
# another way of doing this is in which we don't need to close a file
with open('test.txt', mode="r+") as my_file:

    print(my_file)
    print(my_file.read())

    text = my_file.write("wooooowwwooooooowoooow")

# my_file.close()