# function

# 2 num sun

"""
def sum (a,b):
    print (a+b)

sum(1,3) 

"""
#  --------

def calc_gst(price):
    newprice = price + (price * 0.18)
    return newprice
 
print(calc_gst(200))
print(calc_gst(100))


#  ---------module--------

import math

# print(dir(math))

from math import sqrt

print(sqrt(16))
import random

print(random.random())
print(random.randint(1, 10))
