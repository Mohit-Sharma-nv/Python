import sys
import random

last = sys.argv[1]
num = random.randint(1,10)
if last == num:
    print("You made it ")
else:
    while True:
        your_number = int(input("Enter the Number"))
        if your_number == num:
            print("You made it ")
            break