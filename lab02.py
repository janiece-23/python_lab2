import math
from math import pi

# Part: 1 Variables and Assignments
# 1. Create variables:
name = "Ja Niece Lowery"
age = 23
height = 5.0
favorite_color = "Purple"

# 2. Printing Techniques for variable values:
# 2a. Print one variable at a time:
print(name)
print(age)
print(height)
print(favorite_color)
# 2b. Print with one "print" statement and commas:
print(f"Hello my name is {name},", f"I am {age} years old.", f"I am {height} feet tall and,",
      f"my favorite color is {favorite_color}.")
# 2c. Print with Python formats or format specifiers:
print(f"I love: {favorite_color}.")

# 2e. Print with format specifiers within a multi-line string:
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}
""")
# 3. Create a new variable:
radius = 5
circle_area = pi * radius ** 2
print(round(circle_area))

# Part 2: Statements and Models:
# 1.Calculate the square root:
age_root = math.sqrt(age)
print(age_root)

# 2.Calculate the sine and cosine:
sine = math.sin(height)
cosine = math.cos(height)
print(cosine, sine)

# Part 3: Expressions and Operators


# 1.Arithmetic Operations
sum_age = int(age) + 5
difference = int(height) - 4
product = int(age) * int(height)
quotient = int(height) // 2
remainder = int(age) % 3
raised_age = int(age) ** 2

# 2. Print the results
print(sum_age)
print(difference)
print(product)
print(quotient)
print(raised_age)

# Part 4:Temperature Conversion

# 1. Create a temperature conversion program:
Fahrenheit = 50
Celsius = (Fahrenheit - 32) * 5 / 9
Degrees = Celsius
print(input(Celsius))
