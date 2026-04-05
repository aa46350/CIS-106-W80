#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:25:38 2026

@author: abealansari
"""

# Get Input
widgets_qty = int(input("Enter the quantity of widgets: "))

# Determine price to charge
if widgets_qty > 10000:
    price = 10
elif widgets_qty >= 5000:
    price = 20
else:
    price = 30
    
# Calculate Values
ext_price = widgets_qty * price
tax = ext_price * 0.07
total = ext_price + tax

# Display Results
print(f"Extended price: ${ext_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
