# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:37:44 2022

@author: Cassandra Mendoza
"""

#Part 1 
#develop familarity with arithmetic operators 
print ('Part 1 : arithmetic operators')
y = 9
z = 2
#display values of y and z
print('y ==', y, '; z == ', z)
#add
x = y+z 
print (y, '+' , z, '==', x)
#subtract 
x = y-z
print (y, '-' , z, '==', x)
#multiply
x= y*z
print (y, '*' , z, '==', x)
#integer division 
x= y//z
print (y, '//' , z, '==', x)
#floating point division 
x= y/z
print (y, '/' , z, '==', x)
#mod operator 
x = y%z
print (y, '%' , z, '==', x)
#exponentiation
x = y**z
print (y, '^' , z, '==', x, '\n')

#Part 2 
#develop familiarity with relational operators
print('Part 2: relational operators')
#change the value of z to 9
z= 9 
print ('z now contains', z)
x = (y <=z)
print(y, '<=', z, '==', x)
x = (y < z)
print(y, '<', z, '==', x)
x = (y >= z)
print(y, '>=', z, '==', x)
x = (y > z)
print(y, '>', z, '==', x)
x = (y==z)
print(y, '==', z, '==', x)
x = (y!=z) 
print(y, '!=', z, '==', x)