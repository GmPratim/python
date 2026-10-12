# print all the odd numbers from 1 to 20
"""
for i in range(1,20):
    if i % 2 != 0:
        print(i)
"""

#  print the table of 57

"""
for i in range(1, 11):
    # print( "57 *", i, "=", i * 57)
    print(f"57 * {i} = {i * 57}")

"""
# print all multiples of 3 from 1 to 50 but skip 15.

"""
for i in range (1, 50):
    if i == 15:
        continue
    if i % 3 == 0:
        print(i)
"""

# take two integers as input, find ans print the first number between 1 and 1000 that is divisible by both numbers.

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 1st number: "))

for number in range (1, 1001):
    if number % a == 0 and number % b == 0:
        print (number)
        break
    