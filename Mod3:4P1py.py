#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:05:46 2026

@author: abealansari
"""

# Ask for input
exam1 = float(input("Enter your first exam score: "))
exam2 = float(input("Enter your second exam score: "))

#calculate weighted total
total = (exam1 * .60) + (exam2 * .40)

# Display the result
print("Your total weighted score is:", total)
