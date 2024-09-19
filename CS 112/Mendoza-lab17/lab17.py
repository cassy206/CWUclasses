# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 12:54:31 2022

@author: Cassandra Mendoza
"""

import matplotlib.pyplot as plt
import utilitiesModule as um

def probSuccess( n, k, p):
    """
    Calculates probability of exactly k successes in n independent trial
    where p is the probability of success of a single trial
    n is numTrials
    k is numSuccesses
    p is probability of succcess of a single trial
    """
    #determine the number of subsets of size k that can be created from a set
    #of size n
    nChK = um.nChooseK(n,k)
    #the probability of having exactly k successes when the probability of 
    #a single success is p
    pSuccess = (p**k)
    #the probability of a failure is the probability of a single failure to the 
    #power of (n-k)
    pFail = ((1-p)**(n-k))
    #compute the probability of exactly k successses in n independent trials
    result = nChK * pSuccess * pFail
    return result, pFail, nChK

def plotProb(minN, maxN, k, p):
    """
    Plots the probablities of rolling exactly k instances of a single value
    of a fair dice as the number of trials increases 
    The number of trials ranges from minN up to maxN while k and p are kept constant
    """
    #set up empty lists for the probablities, xValues and probabilities of 
    #failure
    #note that the probablity of success does not change because p and k
    #remain constant
    probs, xVals, pFail, nChKs = [], [], [], []
    #the probability of having exactly k instances is thhe probablity of 
    #a single instance to the power of k
    pSuc = p**k
    #iterate through all the possible values of n, from minN to maxN
    for n in range(minN, maxN +1):
        #append this value of n to the xVals list
        xVals.append(n)
        #invoke the probSuccess function which computes the probablity 
        #for this particular value of n
        pr, fail, nChK = probSuccess(n,k,p)
        #append the probablity of having exactly k successes with this n
        #to the probs list
        probs.append(pr)
        #append the probablity of not having k successses with this n value
        #to the pFail list
        pFail.append(fail)
        #to the nChKs list, append the binomial coefficient for this value of n
        nChKs.append(nChK)
        
    #call function to draw the plots
    drawPlots(xVals, probs, pFail, pSuc, k, nChKs)
    
def drawPlots(xVals, probs, pFail, pSuc, k, nChKs):
    """Assumes the following:
        xVals is python list of x vals
        probs is python list of probs of success
        pFail is pythonlist of probs of failure
        pSuc is p**k
        k is the number of times a specific number is rolle
        nChKs is the binomial coefficient
        """
    #intiate the figure
    plt.figure()
    #plot the probabilities of having exactly k instances of a single value
    plt.plot(xVals, probs, 'k', label = 'prob of exactly ' + str(k) + 'successes')
    #plot the probablitu of failure
    plt.plot(xVals, pFail, 'r' , label = 'p fail')
    #set up the string to annotate the graph with the pSuccess which does
    #not change
    annotStr = 'pSuccess with each trial: ' + str(round(pSuc, 4))
    #set up the title
    titleStr = 'Probablity of exactly ' + str(k) + 'successes as the number of trials varies'
    plt.title(titleStr)
    #annotate with the info in annotStr
    plt.annotate(annotStr, fontsize = 15, xy = (0.25, 0.65) , xycoords = 'axes fraction')
    #set up the x axis label
    plt.xlabel('Num trials')
    #set up the y axis label
    plt.ylabel('Probablity')
    #put the legend in the best position
    plt.legend(loc = 'best')
    
    #make new figure to plot nChKs list
    plt.figure()
    plt.plot(xVals, nChKs, 'g--')
    plt.title('n choose k as n increases; k = ' + str(k))
    plt.xlabel('Num Trials (n)')
    plt.ylabel('Binomial Coefficient (n choose k)')
    
#run the program
#constant for min N, max N and the value of p 
MIN_N = 2
MAX_N = 100
P_VAL = (1/6)

#run with k == 2
k = 2
plotProb(MIN_N, MAX_N, k, P_VAL)

#run with k == 4 
k = 4
plotProb(MIN_N, MAX_N, k, P_VAL)

