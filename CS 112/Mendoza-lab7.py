# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:56:06 2022

@author: Cassandra Mendoza
"""

#collect user input 
strUserInput = input('Enter the binary number to be converted to base ten: ')

#determine the number of chars in the binary 
binLen = len(strUserInput)

print(strUserInput, 'contains' , binLen, "digits")

#initialize intDecVal which will store the base ten number 
intDecVal = 0

#initialize intExpVal to one less than the length of the string 
intExpVal = binLen - 1

#solve by accessing each char in the string 
print('Solve by accessing each char')
for c in strUserInput: 
    #cast the current char to an int
    intCharVal = int(c)
    print('c ==' , c)
    #verify that the intExpVal is correct
    print('intExpVal ==', intExpVal)
    #increasement intDecVal by the correct amount
    intDecVal += (intCharVal * (2**intExpVal))
    print('intDecVal ==', intDecVal)
    #reduce the intExpVal by one
    intExpVal -=1
    
print('binary', strUserInput, 'is equivalent to' , intDecVal, 'base ten\n')

#reset cars
intDecVal = 0
intExpVal = binLen -1

#solve by getting the char at an index value 
print('Solve by accessing a char at specified index value')
for i in range(binLen):
    #cast the current char to an int
    intCharVal = int(strUserInput[i])
    print('i ==',i, 'intCharVal ==' , intCharVal)
    #verify that the intExpVal is correct 
    print('intExpVal ==', intExpVal)
    #increasement intDecVal by the correct amount
    intDecVal += (intCharVal * (2**intExpVal))
    print('intDecVal ==' , intDecVal)
    #reduce the intExpVal by one
    intExpVal -=1
    
print('binary', strUserInput, 'is equivalent to' , intDecVal, 'base ten')
