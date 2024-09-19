# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:33:27 2022

@author: Cassandra Mendoza
"""

#import statements 
import utilitiesModule as um 
import random
import matplotlib.pyplot as plt
import numpy as np

def fairFlip(numFlips):
    """Assumes numFlips is a positive int
    This is fair coin since there is only one 'H' and also only one 'T'
    Therefor the probability of getting an 'H' is (1/2)
    """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads/float(numFlips)

def biasedFlip(numFlips):
    """Assumes numFlips is a positive int
    This is a biased coin since there is two 'H' and also only one 'T'
    Therefor the probability of getting an 'H' is (2/3)
    """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'H', 'T')) == 'H':
            heads += 1
    return heads/float(numFlips)

def flipSim(numFlipsPerTrial, numTrials, blnFair):
    """Function to run the simulation
    assumes numFlipsPerTrial is a positive integer
    Assumes blnFair is a boolean 
    If blnFair is true run with fair coin
    if blnFair is false run with biased coin
    """
    #set up an empty list to contain the results of the simulation
    #this list will contain the fraction of heads obtained with each iteration of 
    fracHeads = []
    #run the simulation
    for i in range(numTrials):
        #run with fair coin
        if blnFair:
            fracHeads.append(fairFlip(numFlipsPerTrial))
        #run with biased coin
        else:
            fracHeads.append(biasedFlip(numFlipsPerTrial))
            
    #determine mean and sd of this data
    mean = sum(fracHeads)/len(fracHeads)
    #use the stdDev function in utilitiesModule to compute this 
    sd = um.stdDev(fracHeads)
    #return the list and the two stats as a tuple
    return(fracHeads, mean, sd)

def labelPlot(numFlips, numTrials):
    """Function to label the histogram"""
    
    plt.title(str(numTrials) + 'trials of' + str(numFlips) + 'flips each: Fair vs Biased coin')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Occurences')
    plt.legend(loc = 'best')
    
def formatOutput(frMean, frStDev, biMean, biStDev, numFlips):
    """Function to format stats from simulations and display in the console"""
    
    #set up a string with which to output stats to console
    infoStr = 'FrMean: ' + str(round(frMean, 4)) + '\nFr SD: ' + str(round(frStDev, 4))\
        + '\nBi Mean: ' + str(round(biMean, 4)) + '\nBi SD: ' + str(round(biStDev, 4))
    print('\nnumFlips:', numFlips)
    print(infoStr)
    
def showHistPlots(simResults, blnFair):
    """Visualize the data generated in a histogram
    Assumes simresults is a list containing the results of running sim with either
    fair or biased coin
    Assumes blnFair is a boolean which specifies whether the coin is fair or biased
    If the blnFair argument is true, this is a fair coin, else a biased coin
    """
    #plot the correct histogram, based on whether blnFair is true or false
    if blnFair:
        plt.hist(simResults, bins = 20, facecolor = 'black' , label = 'Fair')
    else:
        plt.hist(simResults, bins = 20, facecolor = 'red', label = 'Biased')

def showErrorBars(minExp, maxExp, numTrials, blnFair):
    """Assumes mineExp and maxExp positive ints: minExp < maxExp
    numTrials a positive int
    PLots mean fraction of heads with error bars
    minExp and maxExp set the range of numFlipsPerTrial
    For each loop iteration, numFlipsPertrial = 2**exp
    if blnFair == true, runs simulation with fair coins 
    else runs simulation with biased coins
    """
    #create empty lists for the means, sds, and xVals
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp +1):
        #the values on x axis are numFlipsPerTrial
        xVals.append(2**exp)
        #run sim with fair coin
        if blnFair:
            #run sim with fair coins
            fracHeads, mean, sd = flipSim(2**exp, numTrials, True)
        else:
            #run with biased coins
            fracHeads, mean, sd = flipSim(2**exp, numTrials, False)
        means.append(mean)
        sds.append(sd)
        
    #plot the error bars
    if blnFair:
        plt.errorbar(xVals, means, yerr=1.96*np.array(sds), label = 'Fair', color = 'black')
    else:
        plt.errorbar(xVals, means, yerr=1.96*np.array(sds), label = 'Biased', color = 'red')
        
    #fix y axis scale to (0, 1.2)
    plt.ylim(0, 1.2)
    #set the x axis to log scale while maintaining normal scale for y axus
    plt.semilogx()
    plt.title('Mean Fraction of Heads (' + str(numTrials) + ' trials)')
    plt.xlabel('Number of flips per trial')
    plt.ylabel('fraction of heads with 95% confidence limits')
    plt.legend(loc = 'best')
    
def runProgram(flipsPerTrial, minExp, maxExp, numTrials):
    """Function to run the program
    Assumes flipsPerTrial is a list of all the possible flipsPerTrial
    Assumes minExp, maxExp and numTrials are positive integers
    """
    #iterate through the flipsPerTrial list
    for num in flipsPerTrial:
        
        #run sim with fair coin
        fairResults, frMean, frStDev = flipSim(num, numTrials, True)
        #tun sim with biased coin
        biasedResults, biMean, biStDev = flipSim(num, numTrials, False)
        
        #make a new figure to contain both fair and biased histograms 
        plt.figure()
        #show the fair hist
        showHistPlots(fairResults, True)
        #show the biased hist
        showHistPlots(biasedResults, False)
        #label the histogram
        labelPlot(num, NUM_TRIALS)
        
        #output the stats to the console
        formatOutput(frMean, frStDev, biMean, biStDev, num)
        #generate the histograms for both fair and biased 
        #makePLots(num, NUM_TRIALS)
        
        #initiate a new figure for each elememt in flipsPerTrial 
        #this will permit both fair and biased errorBars in one chart
        plt.figure()
        #err bars for fair coin 
        showErrorBars(minExp, maxExp, num, True)
        #err bars for biased coin 
        showErrorBars(minExp, maxExp, num, False)
        
#constant to control numTrials
NUM_TRIALS = 10000
#constats for the x axis values of the error bar plots
MIN_EXP = 3
MAX_EXP = 10

#list of the varying flips per trial
flipsPerTrial = [10, 100, 1000]

runProgram(flipsPerTrial, MIN_EXP, MAX_EXP, NUM_TRIALS)

print('\nPlots are now complete')

