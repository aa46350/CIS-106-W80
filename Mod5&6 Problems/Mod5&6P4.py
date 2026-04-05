#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:59:04 2026

@author: abealansari
"""

# Get Input
principle = float(input("Enter the principle amount of the CD: "))
years = int(input("Enter the years to maturity of the CD: "))

# Determine interest rate
if principle > 100000 and years == 5:
    rate = 0.06
elif 50000 <= principle <= 100000 and years == 10:
    rate = 0.05
elif 50000 <= principle <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

# Calculate first year interest
fy_interest = principle * rate

# Display Results
print(f"Principle: ${principle:.2f}")
print(f"Interest Rate: {rate*100:.0f}%")
print(f"First Year Interest: ${fy_interest:.2f}")
