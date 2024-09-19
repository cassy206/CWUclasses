# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:27:39 2022

@author: Cassandra Mendoza
"""
x = int(input('Enter an int value for x: '))
y = int(input('Enter an int value for y: '))
z = int(input('Enter an int value for z: '))
print()
#Part 1: Version 1: the long, hard way to solve this
print('Solve the problem the long way:')
print ('the largest odd value, or smallest even value, is: ')
if x%2 !=0 and y%2 !=0 and z%2 != 0: 
    print(max(x, y, z))
if x%2 !=0 and y%2 !=0 and z%2 == 0: 
    print(max(x, y))
if x%2 !=0 and y%2 ==0 and z%2 != 0: 
    print(max(x,z))
if x%2 ==0 and y%2 !=0 and z%2 != 0: 
    print(max(y,z))
if x%2 !=0 and y%2 ==0 and z%2 == 0: 
    print(x)
if x%2 ==0 and y%2 !=0 and z%2 == 0: 
    print(y)
if x%2 ==0 and y%2 ==0 and z%2 != 0: 
    print(z)
if x%2 ==0 and y%2 ==0 and z%2 == 0: 
    print(min(x, y, z))
    
#Part 1: Version 2: the more concise way to solve this, plis modifications
#determine largest odd number; if none odd, print smallest
print('Solve the problem in a different way:')
#find the min of the three ints
answer = min(x, y, z)
#initialize bool variable 
oddFound = False
#keep track of how many odds are found 
numOdd = 0
#check all three ints to determine if they are odd
if x%2 != 0:
    answer = x
    oddFound = True
    numOdd += 1
if y%2 != 0:
    oddFound = True
    numOdd += 1
    if y > answer: 
        answer = y
if z%2 != 0:
    oddFound = True
    numOdd += 1
    if z > answer: 
        answer = z
        
#finalize and display results
if not oddFound: 
    print('Neither' , x, 'nor', y, 'nor', z, 'are odd')
    print('The smallest of these values is: ' , answer)
else: if numOdd == 1: 
    print('You entered one odd number, which is' , answer)
else: 
    print('You entered', numOdd, 'odd numbers.')
    print('The largest odd value is ', answer);
    
#Part2: user enters date formatted as mm/dd/yyyy
#slice string and output the three date components 
strInput = input('Enter a date formatted as mm/dd/yyyy:  ')
print('You entered', strInput)
#the chars of the month are at indices 0 and 1
month = strInput[0:2]

#the chars of the day are at indices 3 and 4 
day = strInput[3:5]

#the chars of the year are at indices 6, 7, 8,and 9
year = strInput[6:len(strInput)]

#display the results 
print('month: ', month)
print('day: ', day)
print('year: ', year)

#Part 3:
#collect user input 
strInput = input('Enter an integer value: ')
#determine the data type of strInput
print('The data type of the variable names strInput:', type(strInput), '\n')
#multply strInput by 3
print('Produc of a string and an int: ')
print(strInput, '* 3 == ', (3*strInput), '\n')

#cast the string to an int
intInput = int(strInput)
#determine the data type of intINput 
print('The data type of the variable names intInput: ' , type(intInput), '\n')
print('Product of two ints: ')
print(intInput, '*3 ==' . (3*intInput))

