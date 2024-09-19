# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:57:40 2022

@author: Cassandra Mendoza
"""
#Part 1: Working with strings
print('Part 1:Working with strings')
str1 = 'CWU'
str2 = 'Wildcats'
print(str1)
print(str2)
print('No space character between the two strings: ' + str1 + str2)
print('With space character separating the two strings: ' , str1, str2)
print('Another way to add a space character: ' + str1 + ' ' + str2)

#Part 2:BRANCHING (aka making a decision)
print('Part 2: BRANCHING statements')
print('Part 2, problem 1:use the mod operator to solve a problem')
#collect integer input from the user
#change the input value from a string to an int
number = int(input('Enter an integer value: '))
#use the mod operator to determine whether this is divisible by 3
print('Use == to compare number %3 to zero:')
if number%3 ==0:
    print(number, 'is a multiple of three')
else: 
    print (number, 'is not a multiple of three') 
#add empty line to output, for readability
print ()

#Part 2. problem 1: a different way to do it 
print('This time use the != relational operator')
if number%3 !=0:
    print(number, 'is not a multiple of three')
else: 
    print(number, 'is a multiple of three')
    
#Part 2, problem 2
print('part 2, problem 2: determine if student passes the class:')
#name the cutoff value with all upper case to indicate it should not be changed
CUTOFF_VALUE = 60
#collect input from user 
grade = int(input("Enter the student's grade: "))
if grade >= CUTOFF_VALUE: 
    print("Since the student's grade is " , grade, ". the student passes the class")
else: 
        print("Since the student's grade is " , grade, ". the student does not pass the class")
        
#Part 3: branching statements with boolean variables
print('Part 3: implement branching statements with boolean variables: ')
#set up two string variables 
strSunny = 'Since the sun is shining, we go to the beach'
strRainy = 'Since it is raining, we go to the movies'

#set up boolean variable to store whether or not it is raining 
isRaining = False
if isRaining: 
    print(strRainy)
else: 
    print(strSunny)

print('It started to rain so flip isRaining to True')
isRaining= True
if isRaining: 
    print(strRainy)
else:
    print(strSunny)

#implement the not operator which flips False to True and True to False
print('This time use the not operator')
if not isRaining:
    print(strSunny)
else: 
    print(strRainy)
 
#Part 4: Implement a nested condition
print('Part 4: Implement a nested condition: ')
#boolean variable for whether or not we have the day off from work 
dayOff = True
if dayOff: 
    print('Since we have the day off, what shall we do?') 
    if not isRaining:
        print(strSunny)
    else:
        print(strRainy)
else:
    print('Today we must work, so our day for play must wait.')

print('We just got called in to work today')
dayOff = False
if not dayOff: 
    print ('Today we must work, so our day for play must wait')
else: 
    print('Since we have the day off, what shall we do?')
    if not isRaining:
        print(strSunny)
    else: 
        print(strRainy)
        
#Part 5: type function and newline char
print('Part 5: use the type function to determine the data type of variables: \n')
print('The data type of the variable names str1:' , type(str1), '\n')
print('The data type of the variable named grade: ' , type(grade), '\n')
print('The data type of the variable named isRaining' , type(isRaining), '\n')
