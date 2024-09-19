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
    
    Methods defined here: 
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
        #call the reduce function
        self.reduce()
        
        
        
    
            
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
        Formatting depends on whether the 
        fraction is proper, improper, an integer, or equivilant to one n == d
        """
        #format info to display 
        self.formatImproper()
        whole , remainder = self.formatImproper()
        #proper function
        if self.d == 1:
            return str(self.n)
        elif self.n == self.d:
            #this fraction is the integer one 
            return str(1)
        elif self.n > self.d:
            return str(whole) + ' and ' + str(remainder) + '/' + str(self.d)
        else: 
            return str(self.n) + '/' + str(self.d)

        
    def add(self, f2):
        """Method to return self fraction object plus parameter fraction object"""
        #the n of the product of the two fractions is the product of their numerators
        n = (self.n * f2.d) + (self.d * f2.n)
        #the d of the product of the two fractions is the product of their denominators 
        d = self.d * f2.d
        #instantate fraction object with numerator n and denominator d 
        f3 = Fraction(n,d)
        #return the new fraction 
        return f3
    
    def divide(self, f2):
        """Method to return self fraction object divided by parameter function object"""
        #the n of the product of the two fractions is the product of their numerators 
        n = (self.n * f2.d)
        #the d of the product of the two fractions is the product of their denominators 
        d = self.d * f2.n
        #instantate fraction object with numerator n and denominator 2 
        f3 = Fraction(n,d)
        #return the new fraction 
        return f3
    
    def formatImproper(self):
        """If a fraction is improper(i.e. n > d ) this method determines
        integer value of mixed fraction and the n of the mixed fraction: 
            the d does not change """
        whole = self.n // self.d
        remainder = self.n % self.d
        
        return whole, remainder
        
 
            
            
    def reduce(self): 
        """Method to reduce fraction to its lower terms 
        This is done by first finding the gcd and then dividing 
        both n and d by this value"""
        gcd, numIts = um.gcdIterative(self.n,self.d)
        self.n = self.n // gcd
        self.d = self.d // gcd
       
    
    def subtract(self, f2):
        """Method to return self fraction object minus parameter function object"""
        #the n of the product of the two fractions is the product of their numerators 
        n = (self.n* f2.d) - (self.d * f2.n)
        #the d of the product of the two fractions is the product of their numerators 
        d = self.d * f2.d
        #instantate fraction object with numerator n and denominator d
        f3 = Fraction(n,d)
        #return the new fraction 
        return f3
    
        