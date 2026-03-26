


z = 15 + 9.5j
print (z)
print(type(z))

z1Value = complex(67.9, 122.82)
print(z1Value)

c = complex(10)
print(c)


# Now taking look into Literals , what are the type of literals, WHAT IS Literals
# Integer , Float, Boolean, Complex, String
#   ---> So the direct value that are used in the program are called as Literals
#  --> LITERALS are also called as Constant
#1 example
a = 5
b = 33

# type of literals
('\n -----> Working with Integer Literals')
# Type 1-----> Integer Literals
a = 201
b = 232_103_197
print(a, b)
#  So if you want to write integer literals separated you can separate them with UNDERSCORE(IT is for our use , readability)
('\n -----> Working with Float Literals')
#Type 2 -----> Float Literals
#---> So these are "c = 122E3" its is called scientific representation
a1 = 21.918
print(a1,type(a1))
b1 = 1.792
print(b1,type(b1))
c = 122E3
print(c,type(c))
d = 12.4e-2
print(d,type(d))
('\n -----> Working with Boolean Literals')

#Type 3 -----> Boolean Literals
# --> value i have taken for a = True and b = False
a = True
b = False
print(a,type(a))
print(b,type(b))

A = 2345
B = 3824

if A % 2 == 0 and B % 2 == 0:
    print(True)
else:
    print(False)

('\n -----> Working with Complex Literals')
#Type 4 -----> Complex Literals

a = 4 + 5j
b = 1_2 +5j
print(a,type(a))
print(b,type(b))
c = 234.2 + 232.31j
print(c,type(c))


('\n -----> Working with String Literals')
#Type 5 -----> String Literals
# ---> It suports both SINGLE quote(Commonly we use this one) & DOUBLE quotes and ALSO TRIPLE Quotes
name1 = 'Alexander'
name2 = "ROHIT"
print(name1,type(name1) , name2,type(name2))


print("======<Area of a Circle>======",)
# "Problem Statement Write a Python program to calculate the area of a circle using its given radius.
# Use the math.pi constant to ensure accuracy in the formula for the area of a circle."
import math
r = 10
areaOfCircle = math.pi * math.pow(r, 2)
print(areaOfCircle)

print ("-------------------------")

print("======<Kilometers to Miles>======",)
# "Write a Python program that converts a distance given in kilometers to miles.
# Display the result in a formatted output."

givenKilometers = 15
miles = givenKilometers * 0.621
print("Miles:-",miles)

print ("-------------------------")

print("======<Calculate the Displacement.>======",)
# "Problem Statement - d =  ( v * v  -  u * u ) / (2 * a)
# Write a Python program to calculate the displacement (d) of an object using the second equation of motion:"
import math
u = 4
v = 9
a = 2

getDisplacement = (math.pow(v, 2) - math.pow(u,2)/(2 * a))
print("Displacement is : ", getDisplacement)

print ("-------------------------")

print("======<Calculate the Surface area of Cuboid.>======",)
# "Problem Statement :- Write a Python program to compute the total surface area of a cuboid. Use pre-defined values
# for length, breadth, and height, then calculate the surface area .
#  Formula: Total Surface Area = 2 * (length * breadth + length * height + breadth * height)

l = 28
b = 12
h = 34.233

areaTotalSufaceOfCuboid= 2*(l * b + b * h + l * h)

print("TotalSuface of Cuboid:",areaTotalSufaceOfCuboid)

print ("-------------------------")

print("======<Quadratic Equation.>======",)
# "Problem Statement :- Complete the code to find and print the roots of the quadratic equation:"

import math
a = 6
b = 9
c = 34
root1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
root2 = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)

print("root1:-", root1 and "root2:-" , root2)
