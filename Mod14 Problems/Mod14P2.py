#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:06:23 2026

@author: abealansari
"""

# Define the object
class Student:
    
    def __init__(self, first, last, dist_code, credits):
        self.first = first
        self.last = last
        self.dist_code = dist_code
        self.credits = credits
    
    def comp_tuition(self):
        if self.dist_code.upper() == "I":
            rate = 250.00
        else:
            rate = 500.00
        return self.credits * rate
        
# Instantiate the object 
student1 = Student('John', 'Jones', 'I', 36)
student2 = Student('Jack', 'Black', 'O', 60)

# Use the object
print('Student:', student1.first, student1.last)
print('District Code:', student1.dist_code)
print('Enrolled Credits:', student1.credits)
print(f'Tuition Owed: ${student1.comp_tuition():.2f}\n')

print('Student:', student2.first, student2.last)
print('District Code:', student2.dist_code)
print('Enrolled Credits:', student2.credits)
print(f'Tuition Owed: ${student2.comp_tuition():.2f}\n')
