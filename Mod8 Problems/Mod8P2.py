#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:39:37 2026

@author: abealansari
"""

# Get input
start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
inc_value = int(input("Enter the increment value: "))

# Loop
current = start_value

while current <= stop_value:
    print(current)
    current += inc_value
    
    