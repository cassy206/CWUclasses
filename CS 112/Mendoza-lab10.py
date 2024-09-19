# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:46:07 2022

@author: Cassandra Mendoza
"""

def isValidInteger(strInt):
    """Assumes strInt is a string of len >= 1
    Returns true if all chars of the string are numeric: 
        else returns False
        
    """
    
    #set up named constants for min and max numeric chars
    MIN_UNICODE = ord('0')
    MAX_UNICODE = ord('9')
    
    #initalize bool var to true 
    isValid = True
    
    #iterate through the chars in the string
    for i in range(len(strInt)):
        #determine Unicode val of this char
        charVal = ord(strInt[i])
        #if not in correct range flip isValid to False
        if (charVal < MIN_UNICODE or charVal > MAX_UNICODE):
            isValid = False
            
    return isValid

def getValidInteger () : 
    """
    Implements a loop to iterate until the user enters a valid integer
    in the body of the loop: 
        Prompt the user to enter an integer
        Calls the isValidInteger() function to determine is this is valid numeric 
        Exits the loop when valid input is obtained 
        Returns the string input cast ot an int
    """
    #set up boolean variable to control the loop 
    isValid = False
    
    #intialize strInput 
    strInput = ""
    while (not isValid):
        #get string input from the user 
        strInput = input('Enter an integer: ')
        isValid = isValidInteger(strInput)
        if (not isValid): 
            print('Invalid integer was entered; try again')
    #after exiting the loop return strInput cast to an int
    return int(strInput)

#run the program by calling getValidInteger()
print('Here is a valid integer: ', getValidInteger())
