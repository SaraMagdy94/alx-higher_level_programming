#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

r = abs(number) % 10

if number < 0:
    r = -r

print(f"Last digit of {number:d} is {r:d}", end=" ")

if r > 5:
    print(f"and is greater than 5")
elif r == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
