# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:04:45 2022

@author: Cassandra Mendoza
"""
#import the fraction class 
import fraction 
#import numpy to permit generating random integer values
import numpy as np
#import utlitilesModule to permit getting lists of integer values
import utilitiesModule as um
#empty list to store list of fraction objects
f = []

#set how many fraction objects will be instantieted
NUM_FRACTIONS = 10

#set the min vals for numerator values: keep fractions pos to simplify formatting mix fr.
NUM_MIN_VAL = 2
#set the min vals for denominator values: permit zero to verify that 
#ZeroDivisionError is raised correctly 
DEN_MIN_VAL = 0
#set max val plus one of the numerator vals
NUM_MAX_VAL = 21
#set max val plus one of the denominator vals 
DEN_MAX_VAL = 41
#populate the list of numerator values by calling the getRandomInts in utilitiesModule 
nums = um.getRandomInts(NUM_MIN_VAL, NUM_MAX_VAL, NUM_FRACTIONS)
print('List of numerators : ', nums)

#populate list of denominator values
dens = um.getRandomInts(DEN_MIN_VAL, DEN_MAX_VAL, NUM_FRACTIONS)
print('List of denominators : ' , dens)

print('\nFractions generated: \n')
#instantiate fraction objects by pairing up the num and dens vals 
for i in range (len(nums)):
    try:
        fr = fraction.Fraction(nums[i], dens[i])
        #if the denominator is zero catch the ZeroDivisionError that is raised 
    except ZeroDivisionError: 
        #replace the zero with 1 
        fr = fraction.Fraction(nums[i], 1)
        #inform the user that zero  denominator was changed to 1
        print('Zero denominator changed to 1 at index', i) 
        
       
    #append this fraction object to the list
    f.append(fr)
    
print() #add line of white space in console 
#display all fractions, as both  n/d and as its equivilant float representations 
for i in range (len(f)): 
    print ('i:', i , '; f[' , i , ']:', f[i], ', equivilant to' , f[i].getFloat())


#randomly choose the two fractions for the operations, by randomly generating integer values
#that represent the index values of an element in the list of fraction objects 
print('\nRandomly select two of the Fraction objects on which to perform the multiply operation: ')
### write the code to randomly get indexF1 in correct range 
indexF1 = np.random.randint(0,10)


print('\nf1: The fraction at index' , indexF1, 'is' , f[indexF1])

### write the code to randomly get indexF2 in correct range 
indexF2 = np.random.randint(0,10)
print('\nf2: The fraction at index' , indexF2, 'is' , f[indexF2])

print()
#perform addition on the two fractions 

f3 = f[indexF1].add(f[indexF2])
print(f[indexF1], 'plus' , f[indexF2], '==' , f3, ', equivalent to' , f'{f3.getFloat():,.4f}')
#perform subtraction on the two fractions 
f3 = f[indexF1].subtract(f[indexF2])
print(f[indexF1], 'minus' , f[indexF2], '==' , f3 , ', equivalent to' , f'{f3.getFloat():,.4f}')
#perform multiplication on the two fractions 
f3 = f[indexF1].multiply(f[indexF2])
print(f[indexF1], 'times' , f[indexF2], '==' , f3 , ', equivalent to' , f'{f3.getFloat():,.4f}')

#perform division on the two fractions 
f3 = f[indexF1].divide(f[indexF2])
print(f[indexF1], 'divided by' , f[indexF2], '==' , f3 , ', equivalent to' , f'{f3.getFloat():,.4f}')        