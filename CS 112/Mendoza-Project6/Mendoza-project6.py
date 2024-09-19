# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:33:16 2022

@author: Cassandra Mendoza
"""

#import statements
import utilitiesModule as um
import pandaUtilities as pdu
import matplotlib.pyplot as plt

def plotData(xVals, yVals):
    """Assumes xVals and yVals are equally sized numpy arrays 
    Plots the experimentally observed data
    """
    
    #initiate a new figure for the plot
    plt.figure()
    
    #plot xVals on x axis, yVals on y axis 
    plt.plot(xVals, yVals, 'k',  label = 'Ave AudUsd Prices')
    plt.title('Ave AudUsd Month Prices')
    plt.xlabel('Month')
    plt.ylabel('Price')
    
    plt.legend(loc = 'best')
    
def plotIndexList(inList, yVals):
    """Assumes inList is a numpy array containing the datafram index values of each row
    Assumes yVals is a numpy array of the corresponding values on y axis for each index value
    Plots line plot with inList on x axis and yVals on y axis
    """
    plt.figure()

    #plot inList on x axis and yVals on y axis
    plt.plot(inList, yVals, label = 'AudUsd Ave Month Prices')
    plt.title('AudUsd Ave Month Prices')
    plt.xlabel('Month')
    plt.ylabel('Price')
    plt.legend(loc = 'best')
    
def plotModels(xVals, yVals, pDegrees):
    """Assumes that xVals and yVals are equalily sized numpy arrays, which are the experimentally observed
    Assumes modelDegrees is a python list of the model degrees to be generated and plotted
    """
    
    for n in pDegrees :
        #get the predicted distances from this model
        predictAverages = pdu.getFit(xVals, yVals, n)
        #determine the line style of this model's plot
        strFormatData = um.formatRegressionGraph(n)
        #determine the label of this model
        strLabel = 'model degree: ' + str(n)
        #plot the model
        plt.plot(xVals, predictAverages, strFormatData, label = strLabel)
        
    #verify that the legend is added to the plot
    plt.legend(loc = 'best')
    
#*****END OF FUNCTIONS
inFileName = 'AudUsd.csv'
outFileName = 'AudUsd_ave.csv'

#use the pandaUtilities module function to read the file
#springData is a Panda data frame
dFrm = pdu.readFile(inFileName)

#determine shape of springData
r, c = dFrm.shape

#convert the data  to a numpy array
nHigh = dFrm['High'].to_numpy()
nLow = dFrm['Low'].to_numpy()
#calculate the average
nAverage = (nHigh + nLow)/2

#add to data frame
dFrm['Average'] = nAverage

#use the pandaUtilities writeFile function to write the modified data frame to file
pdu.writeFile(outFileName, dFrm)

#to verify that writing was done correctly read the springDataForve csv file that was written
AudUsd_ave = pdu.readFile(outFileName)

#display the  data frame
print('\nThe modified data frame:\n')
print(AudUsd_ave)

#get numpy arrays
#these will be used for the regression models
nDate = pdu.get_index_list(0, r, AudUsd_ave)
nAverage = AudUsd_ave['Average'].to_numpy()

#plot the experimental data
plotData(nDate, nAverage)

#set up the model degrees to be generated
pDegrees = [1, 3]

#plot the models specified by modelDegrees
plotModels(nDate, nAverage, pDegrees)

#select the columns
start = 20
stop = 80
#this illustrates discussion in text, Figure 20-9
nInhancedDates = pdu.get_index_list(start, stop-1, dFrm)
nInhancedAverages = AudUsd_ave['Average'][20:80].to_numpy()

#plot the reduced data
plotData(nInhancedDates, nInhancedAverages)

#plot the models of the reduced data
#this plot should now be similar to the plot in Figure 20-9
plotModels(nInhancedDates, nInhancedAverages, pDegrees)

#plot the observed distance in relation to the data frame index



