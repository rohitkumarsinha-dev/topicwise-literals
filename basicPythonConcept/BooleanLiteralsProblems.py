print("Boolean Literals Problems")
print('============= Question on Boolean Literals Problems ===============')

# Q1 - Basic True / False assignment
# Assign boolean literals and check their type
# key takeaway--> True and False are bool literals in Python. They are NOT strings — no quotes around them.

is_sunnyDay = False
is_rainingDay = True

print(is_rainingDay)
print(is_sunnyDay)

print('============= Q1 output Above ===============')

# Q2 -bool() constructor on values
# Any value in Python can be converted to bool
# key takeaway--> Rule: 0, None, empty string/list/dict/tuple → False. Everything else → True.

print(bool(1))
print(bool(0))
print(bool("hi"))
print(bool(""))
print(bool([1,2,3]))
print(bool([]))
print(bool(None))

print('============= Q2 output Above ===============')

#-Q3--->Comparison operators return bool
# ---> ==, !=, >, < all evaluate to True or False

x = 36
print("(x) value in boolean", x > 12,)
print("(x) value in boolean", x < 30)
print("(x) value in boolean", x != 10 )
print("(x) value in boolean", x == x )
print("(x) value in boolean", x >= 37)
print("(x) value in boolean", x <= 40 )

result = x > 40
print(type(result), "and result value in boolean" ,result)
print('============= Q3 output Above ===============')

# --Q4-->  Boolean operators: and, or, not
# Combine conditions using logical operators Concept include(and , or, not)
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
print('---Logic to check if age is less than or equal to 21---')
age = 20
has_id = True
print(age <= 21 and has_id)

print('============= Q4 output Above ===============')

#Q5 - bool is a subclass of int
# --> True == 1 and False == 0 in Python Concept Include(bool + int and arithmetic)
# example1 -
print(True == 1) # True
print(False == 0) # True - boolean False showcase '0' so this is why it is true.
print(True + True) # 2
print(True - False) # 1
print(False - False) # 0
print(True * 5) # 5
print(False * 100) # 0

# example2 -
votes = [True, False , False, True, False]
print(sum(votes))
# In Python, bool is a subtype of int.
# This lets you use sum() to count True values in a list — a common real-world trick.
print('============= Q5 output Above ===============')

# Q6 -Short-circuit evaluation
# Python stops evaluating as soon as result is known (This concept Include - short-circuit and efficiency)

def check_aNewValue():
    print("check_a() ran")
    return  False

def check_bNewValue():
    print("check_b() ran")
    return True

# 'and' stops at first False
result = check_aNewValue() and check_bNewValue()
print("Result:", result)

print('-------------')
# 'or' stops at first True
result2 = check_bNewValue() or check_aNewValue()
print("Result2:", result2)

print('============= Q6 output IS Above ===============')


# --Q7 -->  Real-world: login validator
# Combine all concepts in a practical scenario

userName = "rohit"
password = "secure123"
is_active = True

input_user ="rohit"
input_password = "secur@2e123"

user_match = (input_user == userName)
password_match = (input_password == password)
login_ok = user_match and password_match and is_active
print("Login ok:", login_ok)

if login_ok:
    print("welcome:-" ,userName)
else:
    print("Entered Wrong Credentials" )