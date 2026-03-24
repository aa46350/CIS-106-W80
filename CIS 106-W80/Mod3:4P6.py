#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:34:21 2026

@author: abealansari
"""

#Get input
purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current price per share: "))
qty_of_stock = float(input("Enter the number of shares you hold: "))

# Calculate the gain/loss
value_change = (current_price - purchase_price) * qty_of_stock

# Display the result
print("Change in value:", value_change)
