import sys
import random

# Generate a number
start = int(sys.argv[1])
end = int(sys.argv[2])
answer = random.randint(start,end)
print(answer)
while True:
    try:
        num = int(input(f"Enter the number from {start} ~ {end}:  "))
        if start < num < end:
            if num == answer:
                print("You are a Genius!!")
                break
        else:
            print(f"Enter the between {start} ~ {end}")
            continue
    except ValueError:
        print("Enter the number only")
        continue

