# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 16:28:24 2022

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

#display results for bisection search 
print('Use bisection search algorithm to compute square roots of multiples of ', STEP_VAL , 'in the following range: ')
print('[' , START_VAL , ',' , (STOP_VAL - STEP_VAL), ']')
print('Max num iterations required: ' , max(bis_num_it))
print('Min num iterations required: ' , min(bis_num_it))
#average number of iterations, rounded to four plaes 
print ('Ave number of iterations required: ' , round(ave_iterations, 4))
#execution time rounded to six places
print('Bisection search execution time: ' , f'{bis_exe_time:.6f}')
print('***********************************')

#plot histogram illustrating number iterations required for bisection search 
#set up number of bins
bins = 10
#histogram of bis_num_it list
plt.hist(bis_num_it, bins, facecolor = 'green' , label = 'bis_num_it')
#format features of the histogram 
plt.legend(loc = 'upper left')
plt.xlabel('Number of iterations required')
plt.ylabel('Num occurences of each iteration value')
plt.title('Histogram Illustrating Number of Iterations: Bisection Search')
