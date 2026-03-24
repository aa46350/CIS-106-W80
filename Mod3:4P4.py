#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:30:29 2026

@author: abealansari
"""

# Get total amount earned
total_amount = float(input("Enter the total amount earned: "))

# Split evenly between 3 people
each_share = (total_amount / 3)

#Display the result
print("Each person receives:", each_share)
