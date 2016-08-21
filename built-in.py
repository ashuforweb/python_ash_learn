# -*- coding: utf-8 -*-
'''This python file have all the built-in functions of python and their examples.
This file is to be used for reference and explain the functions in more detail view.'''


'''The first built-in function is abs(x): Return the absolute value of a number.
 The single argument may be a plain or long integer or a floating point number.
 If the argument is a complex number, its magnitude is returned.'''
# To explain and examplified this let's initiate x as some number
x = 1
print abs(x) #This will print 1
x = 1.5
print abs(x) #This will print 1.5
x = 1.7267467272723723823
print abs(x) #This will print 1.7267467272723723823
x = complex(1+3j) #This will print magnitude of 1=3j which is calculated as √(1^2+3^2)
print abs(x)

'''This is about all(iterable) function. The single argument is to be iterable and
the output is True if all the elements of iterables are true or iterable is empty else False.'''
theList = []
print all(theList) # This will print True as the iterable list 'theList' is empty
theList = [True,True,True,True,True,True,True,]
print all(theList) # This will print True as all the elements of this list are True.
theList = [True,True,True,False]
print all(theList) # This will print False as not all the elements (last element is False) are not true.

'''This is about any(iterable) function. The single argument is to be iterable and
the output is True if any of the elements of iterables are True else False.'''
theList = [False,False,True,False,False]
print any(theList) # This will print True as 3rd element of the list is true.
theList = []
print any(theList) # This will print False as it's emplty list.
theList = [False,False,False,False]
print any(theList) # This will print False as all elements are False.

'''bin(y) Converts an integer number to a binary string.'''
y = 8
print bin(y) #this will print 0b1000 as this is binary value of 8

'''bool() function returns boolean value of argument will be converted using the standard
Truth testing procedures'''
z = 'Test'
print bool(z) # This will print True as there is something in string z
z = ''
print bool(z) # This will print False as z is empty string
z = 1
print bool(z) # This will pring True as z has a value of 1
z = 0
print bool(z) # This will pring False as z has a value of 0

'''cmp(a,b) function return positive if a>b. returns negative if a<b or returns 0 if a=b'''
a,b = 1,4
print cmp(a,b) #will print negative
a,b = 2,2
print cmp(a,b) #will print 0 as both a and b are same
a,b = 4,1
print cmp(a,b) #will print positive



c = complex(1,2)
print c
