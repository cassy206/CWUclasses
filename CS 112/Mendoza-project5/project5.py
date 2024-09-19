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

def plotHist(subsetSz, oneList):
    """Assumes subsetSz is a positive int
    oneList in the python list to plot
    plotx is a histogram of oneList 
    If subsetSz is 10 color is blue
    if subsetSz is 30, color is red
    """
    
    #set up the number of bins of the histogram
    numBins = 10
    #format the legends
    strLegend = 'subset == ' + str(subsetSz)
    
    #set up the figure for the histogram
    plt.figure(1)
    #histogram of int means
    for size in subsetSizes:
        if size <= 30:
            plt.hist(means, numBins, color = 'red', histtype = 'step' , label = strLegend)
        elif size <= 10:
            #histogram of int means
            plt.hist(means, numBins, color = 'blue', histtype  = 'step', label = strLegend)
        else: 
            pass
        
    #format features of the histogram
    plt.legend(loc = 'best')
    plt.xlabel('Numerical values')
    plt.ylabel('Number of elements in each bin')
    strTitle = 'Display means of subsets of a total of ' + f'{NUM_VALS:,.0f}' + 'random ints'
    plt.title(strTitle)
    
def plotStdDevs(subsetSizes, stdDevs):
    """assumes subsetsizes is a python list of positive ints
    assumes stdDevs is a python list of floats
    plots the line graph with subset sizes on x axis and std devs on y axis
    """
    #set up a new figure for a line graph
    #this figure will display the standard deviation values
    plt.figure(2)
    plt.plot(subsetSizes, stdDevs, 'b^--')
    plt.title('Standard Deviations as Subset Size increases')
    plt.xlabel('Subset Sizes')
    plt.ylabel('Standard Deviation for each Subset Size')
    plt.hlines(means, subsetSizes[1], subsetSizes[-1], colors='k', \
               linestyles = 'solid' , label = 'Random Constants Mean: ' +\
                str(means))
    
    
def plotMeans(subsetSize, means, minVal, maxVal):
    """Assumes subsetSizes is a python list of positive ints
    assumes means is a python list of floats
    plots the line graph with subsetSizes on x axis and means od means on y axis
    """
    
    #set up a new figure for another line graph 
    #this figure will display the mean values
    plt.figure(3)
    plt.plot(subsetSize, means, minVal, maxVal, 'b^--')
    plt.title('Means as Subset Size increases')
    plt.xlabel('Subset Sizes')
    plt.ylabel('The Mean for Each Subset Size')

    
def getAllLists(subsetSizes, numVals, minVal, maxVal):
    """Assumes the following
    subsetSizes is a python list of positive ints
    numVals, minVal and maxVal are positive ints
    these are the 4 arfs for the call to um.intMeans()
    Iterates through all elements of subsetSizes
    for each element in subsetsizes gets a list of means based on this subset size
    plots histograms if subsetsizes is 10 or 30
    returns list of means of the means and stdDevs of the means 
    these will be needed for aditional plots
    """
    #set up empty lists for all the informmation
    allLists = []
    means = []
    mins = []
    maxs = []
    stdDevs = []
    #loop through all elements of subsetSizes lists
    for x in (subsetSizes):
        #get the list of means based on subset size determined by current value of size
        subsetMeans = um.intMeans(numVals, subsetSizes, minVal, maxVal)
        #append to the allLists list
        allLists.append(subsetMeans)
        #get the min and max of this particular list
        oneListMin = min(subsetMeans)
        oneListMax = max(subsetMeans)
    
        #append the oneLIstMin and oneListMax values to the correct list
        mins.append(oneListMin)
        maxs.append(oneListMax)
    
        #get the mean of this particular list
        oneListMean = um.getMean(subsetMeans)
    
        #append the oneListMean value to the list of means
        means.append(oneListMean)
    
        #get the std dev of this list
        oneListStdDev = um.stdDev(subsetMeans)
    
        #append oneListStdDev to the stdDevs 
        stdDevs.append(oneListStdDev)
    
        #print the formatted string with all the stat info
        #call the formatStatsOutput() function
        formatStatsOutput(x, oneListMin, oneListMax, oneListMean, oneListStdDev)
    
        #generate histogram only for subset sizes of 10 and 30
        #call the plothist()
        plotHist()
        
    
    #after exiting loop format features of the histogram 
    #add legend
    plt.legend(loc = 'best')
    #add xlabel
    plt.xlabel('Numerical values')
    #add ylabel
    plt.ylabel('Number of elements in each bin')
    #add title
    strTitle = 'Display means of subsets of a total of ' + f'{NUM_VALS:,.0f}' + 'random ints'
    plt.title(strTitle)
    
    #return the means and stdDevs lists
    #these will be needed to make aditional plots
    return means, stdDevs

#set up constants for the random ints
NUM_VALS = 100000
MIN_VAL = 0
MAX_VAL = 101

#subset list
subsetSizes = []


#call getAllLists to get the lists and plot the histograms
means, stdDevs = getAllLists(subsetSizes, NUM_VALS, MIN_VAL, MAX_VAL)
plotHist(subsetSizes, means)
#plot the stdDevs
plotStdDevs(subsetSizes, stdDevs)
#plot the means
plotMeans(subsetSizes, means, MIN_VAL, MAX_VAL)





