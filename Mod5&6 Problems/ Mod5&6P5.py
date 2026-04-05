#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:18:27 2026

@author: abealansari
"""

# Get Input
tickets = int(input("Enter the number of concert tickets purchased: "))

# Calculate the price per ticket
if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75
 
# Calculate total cost
total_cost = tickets * price

# Display Results
print("Number of Tickets:", tickets)
print(f"Price per Ticket: ${price:.2f}")
print(f"Total Cost: ${total_cost:.2f}")
