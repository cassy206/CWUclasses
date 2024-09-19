# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:02:33 2022

@author: Cassandra Mendoza
"""
""""Driver class to create fractions from class fraction"""
#import the fraction class 
import fraction 
#import numpy to permit generating random integer values
import numpy as np
#import utlitilesModule to permit getting lists of integer values
import utilitiesModule as um
class Fraction(object):
    """
    A fraction object is defined by its numerator and denominator 
    If the denominetor is zero it raises a ZeroDivisionError
    """
    def __init__(self, n, d):
        """
        Create a fraction object which has two instant variables: 
            n for numerator 
            d for denometer
            if d == 0 , rase ZeroDivsionError
        """
        self.n = n
        if d != 0:
            self.d = d
        else: 
            raise ZeroDivisionError('Denominator cannot be zero')
            
    def getFloat(self, numDecPlaces = 4):
        """
        Returns float represenation of this fraction, rounded to 
        numDecPlaces; if no value for numDecPlaces is passed, uses default 4
        """
        return round((self.n/self.d), numDecPlaces)
    
    def multiply(self, f2):
        """Method to return self fraction object times parameter fraction object"""
        # the n of the product of the two fractions is the product of their numerators 
        n = self.n * f2.n
        #the d of the product of the two fractions is the product of their denominators
        d = self.d * f2.d
        #instantate fraction object, with numerator n and denominator d
        f3 = Fraction(n,d)
        #return the new fraction
        return f3
    
    def __str__(self): 
        """Method to display a fraction as n/d 
        if d ==1  display as a whole number 
        if n == d display as the integer one 
        """
        #format info to display 
        # if d == 1 the fraction is a whole number 
        if self.d == 1:
            return str(self.n)
        elif self.n == self.d:
            #this fraction is the integer one 
            return str(1)
        else: 
            return str(self.n) + '/' + str(self.d) 
    
        