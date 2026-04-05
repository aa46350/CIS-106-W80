#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:05:09 2026

@author: abealansari
"""

# Get Input
qty = int(input("Enter the quantity of the item: "))

# Determine unit price
if qty >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00
    
# Calculate Values
ext_price = qty * unit_price
tax = ext_price * 0.07
total = ext_price + tax

# Display Results
print("Quantity:", qty)
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended price: ${ext_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
