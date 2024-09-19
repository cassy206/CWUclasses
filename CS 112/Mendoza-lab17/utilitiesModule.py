# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 15:39:52 2022

@author: Cassandra Mendoza
"""
import numpy as np
import time
#import matplotlib.pyplot to enable plotting histogram 
import matplotlib.pyplot as plt

MIN = 2
MAX_PLUS_ONE = 31
NUM_INTS = 20
NUM_DISPLAY = 10 

def getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS):
    """Assimes the following: 
        min is an int which specifies the smallest random int to generate
        maxPlusOne is an int which specifies one more than largest random int to generate
        numInts is an int which specifies how many random ints to generate 
        Returns the list of random ints
    """
    #start with empty list of random ints
    randInts = []
    #use for loop to iterate to get required number of ints
    for i in range(NUM_INTS): 
        newInt = np.random.randint(MIN, MAX_PLUS_ONE)
        #append newInt to randInts list
        randInts.append(newInt) 
    return randInts 

def displayListSubset (oneList, subsetSize):
    """Assumes oneList is a python list
    subsetSize is a positive int that specifies how many elements of the list to display 
    """
    #set up a list to contain the subst 
    listSubset = []
    for i in range(subsetSize + 1):
        listSubset.append((oneList[i]))
        
    print(listSubset)

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

def factIterative(n):
    """ Assumes n is an int > 0 
    Implements the iterative version of the algorithm 
    Returns n! and the number of iterations required to compute n!
    """
    result = 1
    numIterations = 0
    while n > 1 :
        result *= n 
        n -= 1
        numIterations += 1
    return result 


def gcdIterative(a, b):
    """Assumes a and b are ints
    Implements loop to determine gcd of a and b 
    Returns the gcd and numIterations required to determine this 
    """
    #keep track of numIterations required
    numIterations = 0
    
    #intialize remainder to zero 
    remainder = 0
    
    #implement loop to compute gcd
    while (b != 0):
        remainder = a % b 
        a = b
        b = remainder
        numIterations += 1
        
    #after exiting loop return a and numIterations
    return a, numIterations 

def getGcdIterativeList(listA, listB):
    """Assumes listA and listB are equivalently sized python lists of ints
    Implements iterative gcd method to determine gcd of each pair 
    Returns the following: 
        execution time required 
        list of gcd values
        list of num iterations required
    """
    #intialize list of gcd vals
    gcdList = []
    numIterations = []
    #get start time
    startTime = time.time()
    #iterate through the lists and determine gcd of each pair 
    for i in range(len(listA)):
        curGcd, numIt = gcdIterative(listA[i], listB[i])
        #append this gcd to gcdList
        gcdList.append(curGcd)
        #append this numIterations to the numIterations list
        numIterations.append(numIt)
        
    endTime = time.time()
    itExeTime = endTime - startTime
    #return exe time, gcdList and numIterations list
    return itExeTime, gcdList, numIterations

def getLines(fn):
    """
    Function to read a file and return a list of the lines in the file:
        Assumes fn is a string which is the name of the file
        """
    #open the file so that it can be read 
    nameHandle = open(fn, 'r')
    #create an empty list of lines
    lines =  []
    for line in nameHandle:
        #as each line is read, append this to the list
        lines.append(line)
    #don'r forget to close the file or there will be problems 
    nameHandle.close()
    #return the list of lines
    return lines

def readFile(fn):
    """ 
    Function to read a file and displau each line in the file that has been read
    """
    inFile = open(fn, 'r')
    
    for line in inFile:
        print(line)
    #dont forget to close the file
    inFile.close()
    
def writeFile(fn, lines):
    """
    Assumes fn is a string that is the name of the file to write
    Assumes lines is a list of the lines to write to file
    Writes the list of lines to file 
    """
    #create the file handle
    outFile = open(fn, 'w')
    
    #iterate through the list of lines, appending each on to the file
    for i in range(len(lines)):
        outFile.write(lines[i])
        
    #dont forget to close the file
    outFile.close()
    
def variance(nums):
    """Assumes that nums is a list of numbers. """
    
    mean = sum(nums) / len(nums)
    tot = 0.0
    for x in nums:
        tot += (x - mean)**2
    return tot / len(nums)

def stdDev(nums):
    """
    Assumes that nums is a list of numbers.
    Returns the standard deviation of nums 
    """
    #the std deviation is the square root of the variance 
    return variance(nums)**0.5

def nChooseK(n, k):
    """Assumes n and k are positive integers
    Computes the binomial coefficient of n and k
    Returns the number of subsets of size k that can be constructed from a set
    of size n; assumes order does not matter; i.e. [1,2] and [2,1] are identical
    """
    #the numerator is factorial of n
    num = factIterative(n)
    #the denominator is factorial of k times factorial of (n-k)
    den = factIterative(k) * factIterative((n-k))
    #return the result of integer division:recall that // is integer division
    return num // den


        