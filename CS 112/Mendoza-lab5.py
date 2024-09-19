# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 22:25:32 2022

@author: Cassandra Mendoza
"""

#set up constant for the Golden Ratio
GOLDEN_RATIO = 1.6180339887

#get user input, as a float, for the specified distance 
fltUserInput = float(input('How close to the Golden Ratio must we get  '))

#initialize first three fibs
fib1 = 0
fib2 = 1
fib3 = fib1 + fib2
#assign the first three fibs to a list
fibs = [fib1, fib2, fib3]

#declare and initialize float vars for ratio and diff
fltRatio = fib2/fib1
fltDiff = abs(GOLDEN_RATIO - fltRatio)

#initialize numfibs to keep track of how many we have 
numFibs = len(fibs)

#initialize boolean flag
#Note: diff from lab4
flag = GOLDEN_RATIO > fltRatio


#loop to generate remaining fibs 
while flag: 
    #reassign the fibs 
    fib1 = fib2
    fib2 = fib3
    #the new fib is the sum of previous two 
    fib3 = fib1 + fib2 
    #append the new fib to the fibs list 
    fibs.append(fib3)
    #update numFibs
    numFibs = len(fibs)

#update float vars for ratio and diff 
fltRatio = fib2/fib1
fltDiff = abs(GOLDEN_RATIO - fltRatio)

#update flag 
flag = GOLDEN_RATIO > fltRatio
    
#display results to the user
print('\nTo get within' , fltUserInput, \
      'of the GOLDEN_RATIO requires generating the following' , numFibs, 'fibs:\n')
print(fibs)
print('\nFib generation is now complete.')
