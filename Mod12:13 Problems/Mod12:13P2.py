#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:30:28 2026

@author: abealansari
"""

# Function to display names
def display_names(names, scores):
    print("Names and Scores:")
    for i in range(len(names)):
        print(names[i], "-", scores[i])
        
# Last Names + scores lists
names = ["Jones", "Williams", "Johnson", "O'Connor", "David", "Pierce", "Jenkins", "Shell", "Abrams", "Shelby"]

scores = [89.5, 96, 93, 74, 69, 77,85.3, 98.2, 90, 100]

# Calling functions
display_names(names, scores)
