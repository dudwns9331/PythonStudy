import math as m
import random

name = 'hi'
print(f"hello {name} world")

random_number = m.ceil(random.random() * 3)

print(random_number)

if random_number == 1:
    print("학식")
elif random_number == 2:
    print("배달")
elif random_number == 3:
    print("편의점")
