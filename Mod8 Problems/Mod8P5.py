#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:26:57 2026

@author: abealansari
"""

total_tuition = 0
count = 0

with open("/Users/abealansari/Documents/students.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip() != ""]

for i in range(0, len(lines), 3):
    try:
        name = lines[i]
        district = lines[i+1]
        credits = int(lines[i+2])
    except (IndexError, ValueError):
        print("Skipping bad data:", lines[i:i+3])
        continue

    if district == "I":
        cost = 250.00
    else:
        cost = 500.00

    tuition = credits * cost

    total_tuition += tuition
    count += 1

    print("Student:", name)
    print("Credits:", credits)
    print("Tuition Owed: $", format(tuition, ".2f"))
    print()

average = total_tuition / count if count > 0 else 0

print("Total Tuition Owed: $", format(total_tuition, ".2f"))
print("Number of Students:", count)
