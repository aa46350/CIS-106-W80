#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:26:37 2026

@author: abealansari
"""

class Student:
    
    def __init__(self, first, last, dist_code, credits):
        self.first = first
        self.last = last
        self.dist_code = dist_code
        self.credits = credits
        
        # Dictionary for tuition rates
        self.tuition_rates = {
            "I": 250.00,
            "O": 500.00,
            "X": 800.00,
            "G": 250.00
        }
    
    def comp_tuition(self):
        rate = self.tuition_rates.get(self.dist_code, 500.00)
        return self.credits * rate
    
    def display(self):
        print(f"{self.first} {self.last}")
        print(f"District Code: {self.dist_code}")
        print(f"Credits: {self.credits}")
        print(f"Tuition Owed: ${self.comp_tuition():.2f}")
        print("-" * 30)
        
student1 = Student("John", "Johnson", "I", 36)
student2 = Student("Michael", "Moore", "O", 25)
student3 = Student("Thomas", "Thompson", "X", 14)
student4 = Student("Gabriel", "Iglesias", "G", 60)

# Results
student1.display()
student2.display()
student3.display()
student4.display()
