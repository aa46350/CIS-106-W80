#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:06:02 2026

@author: abealansari
"""

# Define the object
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b
        
# Instantiate the object 
empl1 = Employee('John', 'Jones', 75000)
empl2 = Employee('Jack', 'Black', 100000)

# Use the object
print('Employee First Name:', empl1.first)
print('Employee Last Name:', empl1.last)
print('Employee Email:', empl1.email)
print('Employee Pay:', empl1.pay)
print(f'Employee Bonus: {empl1.bonus(0.20): .2f}')
