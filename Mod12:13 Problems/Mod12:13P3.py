#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:42:24 2026

@author: abealansari
"""

# Function for highest and lowest scores
def find_high_low(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0 
    low_index = 0
    
    for i in range(len(scores)):
        if scores[i] > high_var:  #for the highest
            high_var = scores[i]
            high_index = i
            
        if scores[i] < low_var:     #for lowest
            low_var = scores[i]
            low_index = i
            
    # Results
    print("Highest score:", names[high_index], "-", high_var)
    print("Lowest score:", names[low_index], "-", low_var)
    
# Main code
names = []
scores = []

with open("studentsscores.txt", "r") as file:
    for line in file:
        data = line.split()
        names.append(data[0])
        scores.append(int(data[1]))
        
# Display data
print("Students Scores:")
for i in range(len(names)):
    print(names[i], "-", scores[i])
    
print()

# Calling the function
find_high_low(names, scores)
        