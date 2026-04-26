#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:18:49 2026

@author: abealansari
"""

students = {
    "Johnson": [87, 90, 92],
    "Davis": [69, 72, 75],
    "Moore": [77, 80, 83],
    "James": [95, 93, 98],
    "Michaels": [97, 95, 99],
    "Richards": [92, 90, 97],
    "Koch": [83, 87, 86],
    "Stevens": [88, 92, 90],
    "Tyson": [66, 70, 71],
    "Matthews": [99, 96, 98]
}

# Function for averages
def calc_avgs(student_dict):
    results = {}
    
    total1 = 0
    total2 = 0
    total3 = 0
    count = 0
    
    for name in student_dict:
        grades = student_dict[name]
        
        # Student avg
        avg = (grades[0] + grades[1] + grades[2]) / 3
        results[name] = avg
        
        # Add to totals
        total1 = total1 + grades[0] 
        total2 = total2 + grades[1] 
        total3 = total3 + grades[2] 
        count = count + 1
        
    # Averages
    class_avg1 = total1 / count
    class_avg2 = total2 / count
    class_avg3 = total3 / count
    
    return results, class_avg1, class_avg2, class_avg3

student_avgs, avg1, avg2, avg3 = calc_avgs(students)

print(f"{'Student Name:':<15} {'Average:':<10}")
print("-" * 25)

for name in student_avgs:
    print(f"{name:<15} {student_avgs[name]:<10.2f}")
 
print("\nClass Average per Test:")
print(f"Test 1 Average: {avg1:.2f}")
print(f"Test 2 Average: {avg2:.2f}")
print(f"Test 3 Average: {avg3:.2f}")
