class SuperList(list):

    def __len__(self):
        return 100
    pass

superlist1 = SuperList()

superlist1.append(50)
print(superlist1)
print(len(superlist1))
print(superlist1[0])
print(issubclass(SuperList,list))