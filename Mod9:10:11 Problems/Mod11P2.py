#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:52:01 2026

@author: abealansari
"""

def comp_exams(exam1, exam2, exam3):
    avg_score = (exam1 + exam2 + exam3) / 3
    total_points = exam1 + exam2 + exam3
    
    return total_points, avg_score

last_name = str(input("Enter the student's Last Name: "))
exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))
exam3 = float(input("Enter the third exam score: "))

points, avg = comp_exams(exam1, exam2, exam3)

print("Student's Last Name:", last_name)
print("Total exam points:", format(points, ".2f"))
print("Average exam score:", format(avg, ".2f"))
