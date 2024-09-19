# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:59:28 2022

@author: Cassandra Mendoza
"""
#Write import statements 
import numpy as np
import time
#import matplotlib.pyplot to enable plotting histogram 
import matplotlib.pyplot as plt


#Write a function to get a list of random ints
def getRandomInts(min, maxPlusOne, numInts):
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
        newInt = np.random.randint(min, maxPlusOne)
        #append newInt to randInts list
        randInts.append(newInt) 
    return randInts 
# Write a function that accepts two integer arguments and returns the gcd of the two integers and also the number of iterations to compute the gcd
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

# Write a function to display a subset of a list
def displayListSubset (oneList, subsetSize):
    """Assumes oneList is a python list
    subsetSize is a positive int that specifies how many elements of the list to display 
    """
    #set up a list to contain the subst 
    listSubset = []
    for i in range(subsetSize + 1):
        listSubset.append((oneList[i]))
        
    print(listSubset)



#Write a function that accepts two equally sized lists of integers and returns:• The execution time required
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

MIN = 2
MAX_PLUS_ONE = 51
NUM_INTS = 500000
NUM_DISPLAY = 10
listA = getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)
listB = getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)
itExeTime, gcdList,itNumIt = getGcdIterativeList(listA, listB)



#plot the histogram for the number of iterations
plt.figure()
bins = 10
plt.hist(itNumIt, bins, facecolor = 'green' , label = 'iterative')
plt.legend(loc = 'best')
plt.title("Number of iterations for iterative gcd function")
plt.xlabel('Number of iterations required')
plt.ylabel('Num occurences of each iteration value')

print('First 10 elements of list A :')
displayListSubset(listA, subsetSize = 10)
print('First 10 elements of list B :')
displayListSubset(listB, subsetSize = 10)
print('First 10 elements of iterative gcdList :')
displayListSubset(gcdList, 10)
print('First 10 elements of itNumIt :')
displayListSubset(itNumIt, subsetSize = 10)
print('Iterative method execution time ' , f'{itExeTime:.4f}')


