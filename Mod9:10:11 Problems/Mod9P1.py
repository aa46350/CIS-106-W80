#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 15:06:44 2026

@author: abealansari
"""

# Function to compute total w/ possible discount
def comp_total(qty, price):
    total = qty * price
    
    # 10% discount if over 10k
    if total > 10000:
        total = total * .90
        
    return total

# I & O Section
grand_total = 0

response = input("Do you want to enter data? (Yes/No): ")

while response.lower() == "yes":
    
    qty = float(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    
    # Calling the function
    total = comp_total(qty, price)
    
    # Results
    print("Quantity:", qty)
    print("Price: $", format(price, ".2f"))
    print("Total: $", format(total, ".2f"))
    print()
    
    # Add to grand total
    grand_total += total
    
    # Repeat ask
    response = input("Do you want to enter another item? (Yes/No): ")
    
# Final output
print("Sum of all extended prices: $", format(grand_total, ".2f"))

    
    