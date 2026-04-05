#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:34:47 2026

@author: abealansari
"""

# Get Input
last_name = input("Enter the employees last name: ")
salary = float(input("Enter the employees salary: "))
job_level = int(input("Enter the employees job level: "))

# Determine bonus rate
if job_level >= 10:
    rate = 0.25
elif job_level >= 5:
    rate = 0.20
else:
    rate = 0.10
    
# Compute Bonus
bonus = salary * rate

# Display results
print("Employees last name:", last_name)
print(f"Bonus: ${bonus:.2f}")
