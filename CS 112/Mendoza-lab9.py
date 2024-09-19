# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:19:48 2022

@author: Cassandra Mendoza
"""
#Function to return a Python list of Fibs
def getFibs(numFibs):
    """Assumes num_fibs is a possitive integer which specifies
    the number of fibs to generate.
    Returns the Pythin list of fib numbers
    """
    #initialize list with first two fibs
    fibs = [0,1]
    #for loop to get the rest of the fibs
    #since no step value specified, default step is one
    for i in range(2, numFibs):
        #get the next fib by finding sum of previous two
        nextFib = fibs[i-2] + fibs[i-1]
        #append nextFib to the fibs list
        fibs.append(nextFib)
        
    #after exiting loop, return the list of fibs
    return fibs

def displayFibs(fibs):
    """Assumes fibs is a list containing a subset of the fibs numbers."""
    
    #iterate through the list: print each element 
    for i in range(len(fibs)):
        print('fibs[' , i, ']==' , fibs[i])
    
def displayList(oneList, listName):
    """ Assumes oneList is any Python list: 
        listName is a string which stores the name of the list.
    """
    #iterate through the list, appending the name to the value of the element 
    for i in range (len(oneList)):
        print(listName, '[' , i, '] ==' , oneList[i])
        
#intialize num_fibs
num_fibs = 10
print('call displayFbs which calls getFibs() as the argument: ')
displayFibs((getFibs(num_fibs)))

print('\ncall display_list which calls get_fibs() as the arguement: ')
displayList(getFibs(num_fibs), 'fibs')

print('\ncall display list giving it the strList and strName as arguements')
strList = ['apples', 'grapes' , 'oranges' , 'peaches' ]
strName = 'fruitList'
displayList(strList, strName)

#add pears to the list of fruits 
newFruit = 'pears' 
strList.append((newFruit))

#display the updated list 
print ('\nAfter adding ' + newFruit + ', strList now contains: ')
displayList(strList, strName)

#finger ex section 4.4, page 85
test = lambda x, y: x / y if (y!=0) else None 
x = 9
y = 3 
print('lambda function with x ==' , x , ': y ==' , y , 'returns: ' , test(x, y))
y = 0
print('lambda function with x ==' , x, ': y ==', y, 'returns:' , test(x,y))
y = 3
#call lambda function and swap x and y 
#use f' to format output to six decimal places 
x = 9
y = 3
print ('lambda function with x ==' , y, ':y ==', x, 'returns:' , f'{test(y,x):.6f}')


    