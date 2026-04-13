#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:32:12 2026

@author: abealansari
"""

response = input("Do you want to enter student data? (Yes/No): ")

count = 0

while response.lower() == "yes":
    
    last_name = input("Enter student's last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))
    
    average = (exam1 + exam2) / 2
    
    print("Last Name:", last_name)
    print("Average Score:", format(average, ".2f"))
    print()
    
    count += 1
    
    response = input("Do you want to enter another student? (Yes/No): ")

print("Number of students entered:", count)