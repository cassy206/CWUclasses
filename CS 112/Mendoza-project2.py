# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:24:02 2022

@author: Cassandra Mendoza
"""

#import package needed to compute execution time
import time
#import matplotlib to enable plotting histogram
import matplotlib.pyplot as plt
#lab 2 solution 
#first generate a series of numbers, for which to compute square root
#constants to determine start, stopPlusOneStop, step value for range function
START_VAL = 5
#NOTE: the STOP_VAL is one STEP_VAL beyond the last number generated
STOP_VAL = 5005
STEP_VAL = START_VAL
#first create an empty list
nums = []
#generate all multiple of 5 from 5 to 5000, inclusive 
for i in range(START_VAL, STOP_VAL, STEP_VAL):
    #append each number to the nums list
    nums.append(i)

# Newton-Raphson for square root
#create an empty list for the square roots computed using Newton  
nr_ans = []
#create an empty list for the number of iterations required using Newton
nr_num_it = []
#set the desirec value of epsilon
epsilon = 0.01
#determine the start time at which Newton-Raphson started 
nr_start_time = time.time()

for i in range(len(nums)):
    #each iteration starts with zero
    nr_num_it.append(0)   
    guess = nums[i]/ 2.0
    
    while abs(guess * guess - nums[i]) >= epsilon:
        guess = guess - (((guess ** 2) - nums[i]) / (2 * guess))
        nr_num_it[i] += 1
    
 #determine when Newton search ends
nr_end_time = time.time()
#compute the execution time required to execute bisection search 
nr_exe_time = nr_end_time - nr_start_time
#determine ave number of iterations
nr_sum_iterations = 0
for i in range(len(nr_num_it)):
    nr_sum_iterations += nr_num_it[i]
    
nr_ave_iterations = nr_sum_iterations / len(nr_num_it)

#create an empty list for the square roots computed using bisection search 
bis_ans = []
#create an empty list for the number of iterations required using bisection search
bis_num_it = []
#set the desirec value of epsilon
epsilon = 0.01

#implement bisection search to compute square root of all  the numbers in the nums list
#determined the start time at which bisection search started
bis_start_time = time.time()
#use for loop to iterate through all numbers, computing for each the square root using bisection search
for i in range(len(nums)):
    #begin assignming elements to the list keeping track of number of iterations required
    #each element begins with zero, which will be successively incremented by one with each iteration 
    bis_num_it.append(0)
    #initialize variables needed for bisection search 
    low = 0.0
    high = max(1.0, nums[i])
    ans = (high + low)/2.0
    #iterate the bisection search method until the estimated square root is within epsilon of the correct value
    while abs(ans**2 - nums[i]) >= epsilon:
        #increasement by one this element of the bisNumIt list
        bis_num_it[i] += 1
        #determine in which half of the search space the correct answer is located 
        if ans**2 < nums[i]:
            low = ans
        else:
            high = ans
        #now that the correct area of search space located, update the estimate of the square root (i.e. ans)
        ans = (high + low)/2.0
    #when the diff between the estimate and correct answer is less than epsilon, append this to the bis_ans list
    bis_ans.append(ans)
#determine the time at which the bisection search was completed 
bis_end_time = time.time()

#compute the execution time required to execute bisection search 
bis_exe_time = bis_end_time - bis_start_time
#determine ave number of iterations
sum_iterations = 0
for i in range(len(bis_num_it)):
    sum_iterations += bis_num_it[i]
    
ave_iterations = sum_iterations / len(bis_num_it)

if (nr_exe_time < bis_exe_time):
    print

#display results for bisection search 

print('Use two different algorithms to compute square roots of multiples of ', STEP_VAL , 'in the following range: ')
print('[' , START_VAL , ',' , (STOP_VAL - STEP_VAL), ']')
print('There are ', (STOP_VAL-START_VAL)/STEP_VAL, 'integers in this range')
print('***********************************')
print('BISECTION SEARCH ALGORITHM: ')
print('Max num iterations required: ' , max(bis_num_it))
print('Min num iterations required: ' , min(bis_num_it))
#average number of iterations, rounded to four plaes 
print ('Ave number of iterations required: ' , round(ave_iterations, 4))
#execution time rounded to six places
print('Bisection search execution time: ' , f'{bis_exe_time:.6f}')
print('***********************************')
print('***********************************')
print('NEWTON_RALPHSON ALGORITHIM: ')
print('Max num iterations required: ' , max(nr_num_it))
print('Min num iterations required: ' , min(nr_num_it))
#average number of iterations, rounded to four plaes 
print ('Ave number of iterations required: ' , round(nr_ave_iterations, 4))
#execution time rounded to six places
print('Newton-Ralphson execution time: ' , f'{nr_exe_time:.6f}')
print('***********************************')
if (nr_exe_time < bis_exe_time):
    print('Newton-Ralphson required less time to execute than Bisection Search ')
else:
    print('Bisection Search required less time to execute than Newton-Ralphson')
#plot histogram illustrating number iterations required for bisection search 
#set up number of bins
bins = 10
#histogram of bis_num_it list
plt.hist(bis_num_it, bins, facecolor = 'green' , label = 'bis_num_it')
plt.hist(nr_num_it, bins, facecolor = 'blue' , label = 'nr_num_it')
#format features of the histogram 
plt.legend(loc = 'upper right')
plt.xlabel('Number of iterations required')
plt.ylabel('Num occurences of each iteration value')
plt.title('Number of iterations:  Bisection Search vs Newton-Raphson')