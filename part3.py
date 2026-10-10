# Arithmetic Operator
"""
print(5+2)
print(5/2)
print(5//2)
print(5%2)
print(5 ** 2)

# assignment operator
x = 1
x = x + 5 #6
x += 5
print(x)

# operator precedence

ans = 2 + 5 * 3 # 17
ans = (2 + 5) * 3 # 21

# comparison operators
#  >, <, >=, <=, ==, !=
1 > 2 # false

#  Logical operator

# or, and, not 
# or ----------> if one side is true means true, if both side is false then false
print ((3>5) or (5>6)) # False
print ((6>5) or (5>6)) # True

# and ------> if two side is true then true, otherwise false

print ((6>5) and (7>6)) # True

# not -----> do oposite 
print ( not (3>2)) # false

"""
# Conditional statements 

# age = 24
# if (age >= 18 ) :
#     print("Adult")
# elif age < 18:
#     print("You can't vote")


marks = 60
if marks >= 80:
    print('A')
elif marks < 80 and marks >= 60 :
    print("B")
else:
    print("C")
 

