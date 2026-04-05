#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:54:11 2026

@author: abealansari
"""

# Get Input
part = input("Enter the part number: ")
qty = int(input("Enter the quantity: "))

# Determine unit cost
if part == "10" or part == "55":
    unit_cost = 1.00
elif part == "99":
    unit_cost = 2.00
elif part == "80" or part == "70":
    unit_cost = 3.00
else: 
    unit_cost = 5.00
    
# Calculate total cost
total_cost = qty * unit_cost

#Display results
print("Part Number:", part)
print(f"Unit Cost: ${unit_cost:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
