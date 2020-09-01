#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit == 0:
    print("Last digit of {} is {} and is 0".format(number, digit))
elif number < 0 or digit < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".
          format(number, '-' + str(digit) if number < 0 else digit))
elif digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, digit))
