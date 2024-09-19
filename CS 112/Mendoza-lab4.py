# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:56:08 2022

@author: Cassandra Mendoza
"""
#get user input for the number of fics to generate 
intUserInput = int(input('How many fibs should we generate?  '))

#initialize first three fibs
fib1 = 0
fib2 = 1
fib3 = fib1 + fib2
#assign the first three fibs to a list
fibs = [fib1, fib2, fib3]

#initialize numfibs to keep track of how many we have 
numFibs = len(fibs)

#initialize boolean flab to control the loop 
flag = numFibs < intUserInput

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
    #determine if we now hav enough fibs
    flag = numFibs < intUserInput
    
#display results to the user
print('\nThe first' , intUserInput, 'fibs:\n')
print(fibs)
print('\nFib generation is now complete.')
