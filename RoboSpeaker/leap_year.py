def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 != 0:
            if year % 4 == 0:
                return leap == True

    else:
        return leap == False

    return leap


year = int(input())
print(is_leap(year))