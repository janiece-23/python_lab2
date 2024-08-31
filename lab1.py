import math

# "Problem 1,Arithmetic Operations"
# "Area of a Circle"
print(math.pi * 5 ** 2)
# "Volume of a Sphere"
print(math.copysign(4, 3) * math.pi * 3 ** 3)
# "Hypotenuse of a right-angled triangle"
print(math.sqrt(3) + math.sqrt(4))

# Problem 2:String Manipulation
# Stirng variable containing name
name = 'Janiece Lowery'
print(name)
# Print lenght of name
print(len("Janiece Lowery"))
# Concatenat First and Last Name
print("janiece" + "lowery")
# Convert Name to Upper and lowercase
print(name.upper())
print(name.lower())

# Problem 3: Variable and Data Types
# Create variables to store age, height
height = float(input("62"))
weight = float(input("102"))
bmi = weight / (height * height)
bmi_rounded = round(bmi, 2)
print("janiece's bmi: ", bmi_rounded)
