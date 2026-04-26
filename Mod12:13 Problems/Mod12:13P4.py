#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:43:26 2026

@author: abealansari
"""

# Dictionary of students & grades
students = {
    "Johnson": 87,
    "Davis": 69,
    "Moore": 77,
    "James": 95,
    "Michaels": 97,
    "Richards": 92,
    "Koch": 83,
    "Stevens": 88,
    "Tyson": 66,
    "Matthews": 99,
}

# Header
print(f"{'Student Name':<15} {'Grade':<10}")

total = 0
count = 0

# Print each name and calculate
for name in students:
    grade = students[name]
    print(f"{name:<15} {grade:<10}")
    
    total = total + grade
    count = count + 1
    
# Average
avg = total / count

print("\nClass Average:", avg)
