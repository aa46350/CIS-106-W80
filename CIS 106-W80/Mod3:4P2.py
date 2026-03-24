#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:20:23 2026

@author: abealansari
"""

# Ask for input
ticker_symbol = str(input("Enter the stocks ticker symbol: "))
n_of_shares = float(input("Enter the number of shares held: "))
c_per_share = float(input("Enter the cost per share: "))

# Calculate amount invested
qty_invested = (n_of_shares * c_per_share)

# Display amount invested
print("The amount you've invested is:", qty_invested)
