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

