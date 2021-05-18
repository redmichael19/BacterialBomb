# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:30:37 2021

@author: Shadow
"""

import random

class Agent():
    def __init__(self, ybomb, xbomb, zbomb):
        """
        Create the bacteria agent.
        
        Keyword arguments:
        ybomb -- an integer representing the y coordinate of the bombs location.
        xbomb -- an integer representing the x coordinate of the bombs location.
        zbomb -- an integer representing the z coordinate of the bombs location. 
        """
        self._y = ybomb
        self._x = xbomb
        self._z = zbomb
        
    def move(self):
        """
        Move the bacteria agent.
        Default values for the wind and turbulence. 
        Outdated function that is left in to show the progression. 
        """
        if self._z >= 75:
            a = random.random()
            print(str(a))
            if a < 0.2:
                self._z += 1
            if a > 0.2 and a < 0.9:
                self._z -= 1
            if a > 0.9:
                self._z = self._z
        else: 
            self._z -= 1
        
        b = random.random()
        print(str(b))
        if b < 0.1:
            self._y += 1
        if b > 0.1 and b < 0.2:
            self._y -= 1
        if b > 0.2 and b < 0.25:
            self._x -= 1
        if b > 0.25:
            self._x += 1
            
    def movev2(self, abz_increase, abz_decrease, bbz_increase, bbz_decrease, north, south, west):
        """
        Move the bacteria agent.
        Allows for the user to define the values for the wind and turbulence.
        
        Keyword arguments:
        abz_increase -- an integer between 0 and 100 representing the chance the bacteria will 
        gain 1m in altitude if the bacteria is equal to or higher than the height of the initial 
        bomb location. 
        abz_decrease -- an integer between 0 and 100 representing the chance the bacteria will
        lose 1m in altitude if the bacteria is equal to or higher than the height of the initial
        bomb location. 
        bbz_increase -- an integer between 0 and 100 representing the chance the bacteria will
        gain 1m in altitude if the bacteria is below the height of the initial bomb location.
        bbz_decrease -- an integer between 0 and 100 representing the chance the bacteria will 
        lose 1m in altitude if the bacteria is below the height of the initial bomb location. 
        north -- an integer between 0 and 100 representing the chance the bacteria will move north.
        south -- an integer between 0 and 100 representing the chance the bacteria will move south.
        west -- an integer between 0 and 100 representing the chance the bacteria will move west. 
        """
        if self._z >= 75:
            a = random.randint(1, 100)
#            print(str(a))
            if a <= abz_increase:
                self._z += 1
            if a > abz_increase and a <= (abz_increase + abz_decrease):
                self._z -= 1
            if a > (abz_increase + abz_decrease):
                self._z = self._z
        else:
            c = random.randint(1, 100)
#            print(str(c))
            if c <= bbz_increase:
                self._z += 1
            if c > bbz_increase and c <= (bbz_increase + bbz_decrease):
                self._z -= 1
            if c > (bbz_increase + bbz_decrease):
                self._z = self._z
            self._z -= 1
        
        b = random.randint(1, 100)
#        print(str(b))
        if b <= north:
            self._y += 1
        if b > north and b <= (north + south):
            self._y -= 1
        if b > (north + south) and b <= (north + south + west):
            self._x -= 1
        if b > (north + south + west):
            self._x += 1        
            
    def __str__(self):
        """
        Print the x, y andz coordinates of the bacteria.
        """
        return "x = " + str(self._x) + ", y = " + str(self._y) + ", z = " + str(self._z)