# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 16:35:21 2022

@author: Cassandra Mendoza
"""

import utilitiesModule as um 

#set up constants needed to get lists of random ints
MIN = 2
MAX_PLUS_ONE = 31
NUM_INTS = 5

#fileName 
fileName = 'gcd.csv'

#get the two lists of random ints
listA = um.getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)
listB = um.getRandomInts(MIN, MAX_PLUS_ONE, NUM_INTS)

#get the gcdlist 
itExeTime, gcdList, numIts = um.getGcdIterativeList(listA, listB)

#generate the list of lines to be written to file
#initialize with column headings, delimited by the comma char and ending with the newline char 
gcdLines = [ 'a, ', 'b, ' , 'gcd\n']

#construct the lines to be written to file, delimited by the comma char: dont forget
#to add newline char to each line 
for i in range(len(listA)):
    oneLine = str(listA[i]) + ',' + str(listB[i]) + ',' + str(gcdList[i]) + '\n'
    gcdLines.append(oneLine)
    
#write the gcdLines data to file
um.writeFile(fileName, gcdLines)
print('\nThe file was successfully written\n')

print('Call the readFile ( ) to displau the file that was written: ')
um.readFile(fileName)

#get a list of lines from the file
fileLines = um.getLines(fileName)

#print the column headings: 
print('Diplay the column headings of the file read with getLines() :\n')
print('fileLines[0] == ' , fileLines[0])

print('Process the data in index 1 and beyondd in fileLines:\n')
#format remainder of the lines 
for i in range (1, len(fileLines)):
    #split on the comma char and put the component values in the correct local vars 
    aVal, bVal, gcdVal = fileLines[i].split(',')
    print('For a ==', aVal, 'and b ==', bVal, ', gcd ==' , gcdVal)
    