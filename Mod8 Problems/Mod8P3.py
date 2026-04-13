#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:48:08 2026

@author: abealansari
"""

with open("employees.txt", "r") as file:
    total_bonus = 0
    
    for line in file:
        data = line.split()
        
        if len(data) < 2:
            continue

        last_name = data[0]
        salary = float(data[1])

        if salary >= 100000:
            rate = 0.20
        elif salary >= 50000:
            rate = 0.15
        else:
            rate = 0.10

        bonus = salary * rate
        total_bonus += bonus

        print(f"{last_name} Salary: ${salary:.2f} Bonus: ${bonus:.2f}")

print(f"\nTotal Bonuses Paid: ${total_bonus:.2f}")
