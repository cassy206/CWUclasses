# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:31:35 2022

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
    plt.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    
    plt.legend(loc = 'best')
    
   
def plotIndexList(inList, yVals):
    """Assumes inList is a numpy array containing the datafram index values of each row
    Assumes yVals is a numpy array of the corresponding values on y axis for each index value
    Plots line plot with inList on x axis and yVals on y axis
    """
    plt.figure()
    
    #plot inList on x axis and yVals on y axis
    plt.plot(inList, yVals, 'bo', label = 'Measured displacements')
    plt.title('Measure Displacement of Spring')
    plt.xlabel('Data frame index value of the force component')
    plt.ylabel('Distance (meters)')
    plt.legend(loc = 'best')
    
def plotModels(xVals, yVals, modelDegrees):
    """Assumes that xVals and yVals are equalily sized numpy arrays, which are the experimentally observed
    Assumes modelDegrees is a python list of the model degrees to be generated and plotted
    """
    
    for n in modelDegrees :
        #get the predicted distances from this model
        predictDistances = pdu.getFit(xVals, yVals, n)
        #determine the line style of this model's plot
        strFormatData = um.formatRegressionGraph(n)
        #determine the label of this model
        strLabel = 'model degree: ' + str(n)
        #plot the model
        plt.plot(xVals, predictDistances, strFormatData, label = strLabel)
        
    #verify that the legend is added to the plot
    plt.legend(loc = 'best')
    
#*****END OF FUNCTIONS

#constant for the acceleration due to gravitt on earth
GRAV_EARTH = 9.81

inFileName = 'springData.csv'
outFileName = 'springDataForce.csv'

#use the pandaUtilities module function to read the file
#springData is a Panda data frame
springData = pdu.readFile(inFileName)

#determine shape of springData
r, c = springData.shape

#convert the data in the Mass column to a numpy array
nMass = springData['Mass(kg)'].to_numpy()

#calculate the force from the mass by multiplying by the grav earth constant
nForce = nMass ** GRAV_EARTH

#add the nForce array to the springData data frame
springData['Force (Newtons)'] = nForce

#use the pandaUtilities writeFile function to write the modified data frame to file
pdu.writeFile(outFileName, springData)

#to verify that writing was done correctly read the springDataForve csv file that was written
springDataForce = pdu.readFile(outFileName)

#display the springDataForce data frame
print('\nThe modified data frame:\n')
print(springDataForce)

#get numpy arraysfor the distance and the force columns in the springDataForce data frame
#these will be used for the regression models
nDistance = springDataForce['Distance(m)'].to_numpy()
nForce = springDataForce['Force (Newtons)'].to_numpy()

#plot the experimental data
plotData(nForce, nDistance)

#set up the model degrees to be generated
modelDegrees = [1, 3]

#plot the models specified by modelDegrees
plotModels(nForce, nDistance, modelDegrees)

#select the columns leaving out last six data points
#this illustrates discussion in text, Figure 20-9
reducedDistances = springDataForce['Distance(m)'][:-6].to_numpy()
reducedForces = springDataForce['Force (Newtons)'][:-6].to_numpy()

#plot the reduced data
plotData(reducedForces, reducedDistances)

#plot the models of the reduced data
#this plot should now be similar to the plot in Figure 20-9
plotModels(reducedForces, reducedDistances, modelDegrees)

#plot the observed distance in relation to the data frame index
springDataIndex = pdu.get_index_list(0, r, springDataForce)

print('\nnumpy array of row index values: \n')
print(springDataIndex)

plotIndexList(springDataIndex, nDistance)

