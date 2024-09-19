# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:20:49 2022

@author: Cassandra Mendoza
"""
print('Problem 1. Generate a list of multiples of 4 from -20 to +16: ')
numList = []
intStart = -20
intStop = 20
intStep = 4
for x in range(intStart, intStop, intStep):
    numList.append(x)
    
#display the list
print('Multiples of' , intStep, 'in the range [ ' , intStart, ',' , (intStop - intStep), '\n')
print(numList)
print()

#now display the list in the opposite order
numList.reverse()
print('Display the list in reverse :\n')
print(numList)
print()

#Problem 2: Generate a list of multiples of 4 from 20 to -16
print('Problem 2. Generate a list of multiples of 4 from 20 to -16: ')
numList = []
intStart = 20
intStop = -20
intStep = -4
for x in range(intStart, intStop, intStep):
    numList.append(x)
    
#display the list
print('Multples of' , intStep, 'in the range [' , intStart, ',' , (intStop - intStep), ']\n')
print(numList)
print()


#problem 3. Generate a list of integers from 21 to -18(has a bug) 
print('Problem 3: Generate a list of integers from 21 to -18:')
print('This code has a bug; ')
print('Find and fix the bug' )
numList = []
intStart = 21
intStop = -21
intStep = -3
for x in range(intStart, intStop, intStep):
    numList.append(x)
    
#displau the list 
print('Integers in the range [' , intStart, ',' , (intStop-intStep), ']\n')
print(numList)

#problem 4
print('Problem 4: Given a single argument to the range function')
intStop = 10
numList = []
for x in range (intStop) :
    numList.append(x)
    
    #display the list
    print('\nIntegers in the range [0 ,' , (intStop -1 ), ']')
    print(numList)
    print()
    
#set up a new list to contain elements squared
newList = []
for x in range(len(numList)):
    newList.append(numList[x]**2)
    
    print('Each element of numLIst swquared:') 
    print(newList)
