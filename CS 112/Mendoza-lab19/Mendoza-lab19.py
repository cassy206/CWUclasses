# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:34:21 2022

@author: Cassandra Mendoza
"""

import numpy as np
import utilitiesModule as um 
import matplotlib.pyplot as plt

def getData(fileName):
    """Function to read data from the springData.csv file
    Assumes fileName is a string for the name of the file being rea
    Returns python lists of the distances and mass read from the file
    """
    #use the getLines fn in um to geta list of the lines in the file
    lines = um.getLines(fileName)
    
    #set up empty lists for distances and masses
    distances, masses = [], []
    
    #process data in the lines, skippiing the first which is col headings
    for i in range(1, len(lines)):
        #spit each line on the space character and assign to correct variables
        d, m = lines[i].split(',')
        #append this line's data to the correct list
        distances.append(float(d))
        masses.append(float(m))
        
    #return the two lists
    return distances, masses

def plotExpData(xVals, yVals):
    """Function to plot experimental data: forces, not forces on x axis, distances on y
    """
    #plot the data
    plt.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    #annotate the plot
    plt.title('Measured Displacement of Spring')
    plt.xlabel('|Force| (Newtons)')
    plt.ylabel('Distance (meters)')
    
def plotModels(forces, distances, forces2, pDegrees):
    """Assumes:
        forces is numpy array of experimental x vals
        distances is numpy array of experimental y vals
        forces2 is the numpy array of experimental data plus the extra 1.5 kg mass
        pDegrees is python list of regression models to plot
        """
        
    #iterate through all values of n in pDegrees
    for n in pDegrees:
        #get the coefficients for this model
        fit = np.polyfit(forces, distances, n)
        #get the predicted distances for this regression degree, including the extra 1.5 kg mass
        predictedDist = np.polyval(fit, forces2)
        #first get the correct line style
        strLineStyle = um.formatRegressionGraph(n)
        strLegend = 'regression model:' + str(n)
        #plot this model
        plt.plot(forces2, predictedDist, strLineStyle, label = strLegend)
        
    #add the legend
    plt.legend(loc = 'lower left')
    
def runProgram(inputFile, pDegrees):
    """Function to run the program
    Assumes:
        inputFile is a string which is the name of the file being read
        pDegrees is python list of model degrees
        """
    #constant for the acceleration due to gravity on earth(m/s**2)
    GRAV_EARTH = 9.81
    
    #mass not included in the data file
    addMass = 1.5
    
    #read the file and store the data in the lists distances and masses
    distances, masses = getData(inputFile)
    
    #convert the distances list to a numpy array
    distances = np.array(distances)
    
    #convert the masses list to a numpy array
    masses = np.array(masses)
    
    #multiply all elements in the masses array by GRAV_EARTH constant
    #thus creating the new numpy array forces
    forces = masses * GRAV_EARTH
    
    #compute the force of additiona; weight's mass
    addForce = addMass * GRAV_EARTH
    
    #append this element to the forces numpy array, thus creating a new array
    #which now has 20 instead of 19 elements
    forces2 = np.append(forces, [addForce])
    
    #plot the experimental data, which does not include the 1.5 kg mass
    plotExpData(forces, distances)
    
    #plot the models, including the extra mass
    plotModels(forces, distances, forces2, pDegrees)
    
    
#set the model degrees to run
pDeg = [1, 2, 3]

#run the program
runProgram('springData.csv', pDeg)
