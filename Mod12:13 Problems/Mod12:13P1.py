#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 13:51:10 2026

@author: abealansari
"""

# Function to display names
def display_names(names):
    print("Names in order:")
    for i in range(len(names)):
        print(names[i])

# Function to display in reverse order
def display_reverse(names):
    print("\n Names in reverse order:")
    for i in range(len(names)-1, -1, -1):
        print(names[i])
        
# Last Names list
names = ["Jones", "Williams", "Johnson", "O'Connor", "David", "Pierce", "Jenkins", "Shell", "Abrams", "Shelby"]

# Calling functions
display_names(names)
display_reverse(names)
