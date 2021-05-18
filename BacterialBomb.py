# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:11:21 2021

@author: Shadow
"""

# Import required modules
import csv
import matplotlib
import agentframework


# Key variables
zbomb = 75
bomb_location = []
no_of_bacteria = 1


# Reads in the wind.raster file as a 2D list.
f = open('wind.raster.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    bomb_location.append(rowlist)
f.close()

# 2D loop of the bomblocation to identify the bomb location.
# Variables ybomb and xbomb are created which are the
# y and x coordinates respectively. 
for i in range(len(bomb_location)):
    for j in range(len(bomb_location[i])):
        if bomb_location[i][j] == 255.0:
            print("Bomb location: y = " + str(i) + ", x = " + str(j))
            ybomb = i
            xbomb = j


# Creation of a 2D list to store the final location.
# This will be used to create the density map. 

final_bacteria_locations = []
for i in range(300):
    rows = []
    for j in range(300):
        rows.append(0.0)
    final_bacteria_locations.append(rows)


# Creates a single bacteria. 
# Inputs relate to the x, y and z coordinates of the bomb location.
# bacteria = agentframework.Agent(ybomb, xbomb, zbomb)

bacteria_count = 1
while (bacteria_count <= no_of_bacteria):
    bacteria = agentframework.Agent(ybomb, xbomb, zbomb)
    while (bacteria._z > 0):
        bacteria.move()
        print(str(bacteria))
    final_bacteria_locations[bacteria._y][bacteria._x] += 1
    bacteria_count += 1
    print(str(bacteria))
    
    
    
matplotlib.pyplot.imshow(final_bacteria_locations)

    
    
    