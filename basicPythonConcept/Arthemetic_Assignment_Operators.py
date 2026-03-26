print("What is Arithmetic Assignment Operator is:-"
      " is a shorthand way to perform an arithmetic operation "
      "and assign the result back to the same variable in one step")

# Addition + Assignment +=
print("<-----1(Addition + Assignment, +=)------>")
b = 123
x = 13
a = 1
c = 1
c += a * (b * x)  #c = c + a *(b * x)
print(c)

print("<-----2(Substraction + Assignment,  -=)------>")
# Substraction + Assignment -=
b = 124
x = 14
a = 2
c = 1
c -= a * (b * x)  #c = c - a *(b * x)
print(c)

print("<-----3(Multiplication + Assignment,  *=)------>")
# Multiplication + Assignment,  *=
b = 125
x = 15
a = 3
c = 6
c *= a * (b * x)  #c = c * a *(b * x)
print(c)

print("<-----4(True division +  Assignment,  /=)------>")
# True division +  Assignment,  /=
b = 15
x = 20
a = 3.2
c = 6
c /= a * (b * x)  #c = c / a *(b * x)
print(c)

print("<-----5(Floor division + Assignment,  //=)------>")
# Floor division + Assignment,  //=
b = 1.5
x = 2.5
a = 3.2
c = 6
c //= a * (b * x)  #c = c // a *(b * x)
print(c)

print("<-----6(Modulo + Assignment,  %=)------>")
# Modulo + Assignment,  %=
b = 1.5
x = 2.5
a = 3.2
c = 6
c %= a * (b * x)  #c = c % a *(b * x)
print(c)

print("<-----7(Exponentiation + Assignment,  **=)------>")
# Modulo + Assignment,  **=
b = 1.235
x = 2.52
a = 3.292
c = 6.222
c **= a * (b * x)  #c = c ** a *(b * x)
print(c)