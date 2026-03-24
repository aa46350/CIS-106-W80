#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:25:20 2026

@author: abealansari
"""

# Ask for input
last_name = str(input("Enter your last name: "))
midterm_score = float(input("Enter your midterm exam score: "))
final_score = float(input("Enter your final exam score: "))

# calculate total exam points
total = (midterm_score * .40) + (final_score * .60)

# Display last name and total exam points
print("Student:", last_name)
print("Total exam points:", total)
