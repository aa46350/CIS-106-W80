#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:42:28 2026

@author: abealansari
"""

# Function for batting average
def comp_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

# Main Code
count = 0

response = input("Do you want to enter player data? (Y,N): ").lower()

while response in ("y", "yes"):
    
    last_name = input("Enter the player's last name: ")
    hits = int(input("Enter the number of hits: "))
    at_bats = int(input("Enter the number of at bats: "))
    
    # Calling the function
    average = comp_average(hits, at_bats)
    
    # Results
    print("Last Name:", last_name)
    print("Batting Average: ", format(average, ".3f"))
    print()
    
    count += 1
    
    # Repeat ask
    response = input("Do you want to enter another player? (Y/N): ").lower()
    
# Final Output
print("Number of player's entered:", count)
