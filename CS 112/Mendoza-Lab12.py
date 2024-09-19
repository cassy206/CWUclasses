# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 20:59:34 2022

@author: Cassandra Mendoza
"""
numRecCalls = 0
#collect user input 
n = int(input('enter the integer for which you wish to compute the factorial: '))
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
    return result, numIterations 

 


def factRecursive(n):
    """ Assumes n is an int > 0
    Implements the recursive version of the algorithm 
    With each recursive call, increments global numRecCalls by one
    Returns n! 
    """
    
    #indicate that this is the global var being accessed this is not a local variable 
    global numRecCalls
    #increment numRecCalls by 1
    numRecCalls += 1
    if n == 1:
        return n
    else: 
        return n * factRecursive(n-1)

    
result, numIterations = factIterative(n)
factRecursive(n) 




#use the iterative version of the algorithm 
print('\nUsing the itterative version of the algorithm : \n')
print(n , ' !==' , f'{result:,.0f}')
print('\nThis computation required' , numIterations, 'iterations of the loop to solve,')


#use the recursive version of the algorithm 
print('\nUsing the recursive version of the algorithm : \n')
print(n , ' !==' , f'{result:,.0f}')
print('\nIt required' , numRecCalls , 'recursive calls to solve the problem,')

