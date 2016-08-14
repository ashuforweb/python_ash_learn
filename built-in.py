# -*- coding: utf-8 -*-
'''This python file have all the built-in functions of python and their examples.
This file is to be used for reference and explain the functions in more detail view.'''


'''The first built-in function is abs(x): Return the absolute value of a number.
 The argument may be a plain or long integer or a floating point number.
 If the argument is a complex number, its magnitude is returned.'''
# To explain and examplified this let's initiate x as some number
x = 1
print abs(x) #This will print 1
x = 1.5
print abs(x) #This will print 1.5
x = 1.7267467272723723823
print abs(x) #This will print 1.7267467272723723823
x = complex(1+3j) #This will return magnitude of 1=3j which is calculated as √(1^2+3^2)
print abs(x)
