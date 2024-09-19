# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:46:29 2022

@author: Cassandra Mendoza
"""

import utilitiesModule as um

#call the um.getValidInteger () function to get a valid integr value
x = um.getValidInteger()

print('\nYou entered: ' , x, '\n')

#determine the factorial of the user's input: 
result, numIterations = um.factIterative(x)
print(str(x) + '! == ' + f'{result:,.0f}')

#call the um.getGcdlist() which generates two random number lists and 
#a list of their gcd vals 
#first set up the constants needed for arguements 
MIN = 2
MAX_PLUS_ONE = 31
NUM_INTS = 20
NUM_DISPLAY = 10 

print('\nGenerate two random int lists and a list of their gcd values: ')

listA = um.getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)
listB = um.getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)

#call the um.getGCDLIST() function to get the list of gcd vals
itExeTime, gcdList,itNumIt = um.getGcdIterativeList(listA, listB)

#print the three lists 
print('\nThe first' , NUM_DISPLAY , 'elemnts of list A:\n')
um.displayListSubset(listA, NUM_DISPLAY)

print('\nThe first' , NUM_DISPLAY , 'elemnts of list B:\n')
um.displayListSubset(listB, NUM_DISPLAY)
    
print('\nThe first' , NUM_DISPLAY , 'elemnts of gcdLIst:\n')
um.displayListSubset(gcdList, NUM_DISPLAY)