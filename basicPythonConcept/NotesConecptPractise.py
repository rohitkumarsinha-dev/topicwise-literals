
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
