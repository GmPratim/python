# range
# range(5) # 0,1,2,3,4

# 1 to 5
range(1, 6)
# print(range(6))


# range(start, stop, step)

# ---------------------------
# while loop
"""
counter = 1
while counter <= 5:
    print("Pratim")

i = 5
while i > 0:
    print(i * "*")
    i -= 1
"""

# ----------------------------
# for loop

# 0 t 4
# for i in range(5):
#     print(i)
# ---------------------------
# 1 to 5
# for j in range(1, 6):
#     print("num", j)

# -------------------
# 1 to 10 - even
"""
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

"""

# break & continue

#  multiple of 3 [1 to 50] => 21 

for i in range(1, 50):
    if(i == 21):
        # break
        continue
    if i % 3 == 0:
        print (i)
        