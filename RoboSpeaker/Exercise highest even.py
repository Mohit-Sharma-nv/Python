def highest_even(li):
    highest = 0
    for item in li:
        if item%2==0:
            if item >= highest:
                highest = item
    return highest
    pass

print(highest_even([10,20,3,4,8,11,]))


def high_even(list1):
    even = []
    for item in list1:
        if item %2 ==0:
            even.append(item)
    return max(even)

print(high_even([10,210,3,4,8,11,]))