#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

div = number % 10
if number < 0:
    div = div - 10
elif div > 5:
    print("Last digit of", number, "is", div, "and is greater than 5")
if div < 0:
    print("Last digit of", number, "is", div, "and is less than 6 and not 0")
elif div == 0:
    print("Last digit of", number, "is", div, "and is 0")
