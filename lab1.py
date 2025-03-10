import math
from collections.abc import async_generator

radius = 5
area_of_circle = math.pi * radius ** 2
print(area_of_circle)

volume = (4/3) * math.pi * radius ** 3
print(f"the circle radius is {volume: .2f}")

a = 3
b = 4
c = math.sqrt(a**2 + b**2)
print(c)

first_name = 'Adriel'
Last_name = 'Bennett'
Full_name = first_name + Last_name
len_name = len(first_name + Last_name)
print(f'the length of {Full_name} {len_name}')
print(f'Name lower case {Full_name.lower()} Name upper case {Full_name.upper()}')

age = 45
height = 6.0
height_inch = height * 12
weight = 210

bmi = (weight / height_inch**2) * 703
print(f"{Full_name.upper()}'s BMI is {bmi}")