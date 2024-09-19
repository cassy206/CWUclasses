# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:29:05 2022

@author: Cassandra Mendoza
"""

#import the utilities module
import utilitiesModule as um
#import matplotlib.pyplot to enable generating histogram of the data
import matplotlib.pyplot as plt

def formatStatsOutput(subsetSz, minVal, maxVal, meanVal, sdDevVal):
    """Assumes all args are positive ints
    Prints a string with all the arfs properly formatted
    Floats are rounded to two decimal places
    """
    strOutput = 'Size of each subset: ' + str(subsetSz) +\
        '\nMin: ' + f'{minVal:.2f}' +\
        '\nMax: ' + f'{maxVal:.2f}' +\
        '\nMean: ' + f'{meanVal:.2f}' +\
        '\nStd dev: ' + f'{sdDevVal:.2f}'
    print(strOutput)
    
def getStats(numVals, subsetSz, minVal, maxVal):
    """Assumes all args are positive ints
    Function generates list of means of the subsets and calculates the stas
    returns the following:
        min mean value
        max mean value
        mean of the means
        std dev of the means
        """
    #get the list of means of random ints of this subset size
    meanInts = um.intMeans(numVals, subsetSz, minVal, maxVal)
    
    #determine the smallest and the largest of the means in the list
    meanMin= min(meanInts)
    meanMax= max(meanInts)
    
    #determine the mean of all the means
    mean_of_means = um.getMean(meanInts)
    #determine std dev of all the means 
    meanStdDev = um.stdDev(meanInts)
    
    return meanInts, meanMin, meanMax, mean_of_means, meanStdDev

def plotHistograms(meansSmall, subsetSizeSmall, meansLarge, subsetSizeLarge):
    """Assumes the two args are equally sized python lists of means
    plots both in a single histogram of hist type = 'step'
    """
    
    #set up the number of bins of the histogram
    numBins = 10
    
    #format the legends
    strLegendSm = 'subset == ' + str(subsetSizeSmall)
    strLegendLg = 'subset == ' + str(subsetSizeLarge)
    
    #set up the figure for the histogram
    plt.figure()
    #histogram of int means with small subset size
    plt.hist(meansSmall, numBins, color = 'blue', histtype = 'step' , label = strLegendSm)
    #histogram of int means with large subset size
    plt.hist(meansLarge, numBins, color = 'red', histtype  = 'step', label = strLegendLg)
    #format features of the histogram
    plt.legend(loc = 'best')
    plt.xlabel('Numerical values')
    plt.ylabel('Number of elements in each bin')
    strTitle = 'Display means of subsets of a total of ' + f'{NUM_VALS:,.0f}' + 'random ints'
    plt.title(strTitle)
    
#set up constants for the random ints
NUM_VALS = 100000
MIN_VAL = 0
MAX_VAL = 101

#ask the user the size of two subsets; one small and one large
print('Enter a small size of each subset: ')
subsetSizeSmall = um.getValidInteger('')
print('Enter a larger size of each subset: ')
subsetSizeLarge = um.getValidInteger('')

#get the list and stats for the small subsize
meanIntsSmall, min_small, max_small, mean_small, stdDev_small = getStats(NUM_VALS, subsetSizeSmall, MIN_VAL, MAX_VAL)
meanIntsLarge, min_large, max_large, mean_large, stdDev_large = getStats(NUM_VALS, subsetSizeLarge, MIN_VAL, MAX_VAL)

#format and print to console the stats
print('\nSMALL SUBSET INFO:')
formatStatsOutput(subsetSizeLarge, min_large, max_large, mean_large, stdDev_large)

#plot both histograms
plotHistograms(meanIntsSmall, subsetSizeSmall, meanIntsLarge, subsetSizeLarge)
