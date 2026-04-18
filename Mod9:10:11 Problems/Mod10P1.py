#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:25:17 2026

@author: abealansari
"""

# Function for next months forecast
def comp_forecast(month, sales):
    
    #forecast percentages
    if month in ("january", "february", "march"):
        percent = .10
    elif month in ("april", "may", "june"):
        percent = .15
    elif month in ("july", "august", "september"):
        percent = .20
    elif month in ("october", "november", "december"):
        percent = .25
    else:
        percent = 0
        
    # Comp next months sales
    forecast_sales = sales * (1 + percent)
    
    return forecast_sales

# Main code
count = 0

response = input("Do you want to enter sales data? (Y/N): ").lower()

while response in ("y", "yes"):
    
    last_name = input("Enter Last Name: ")
    month = input("Enter month (Jan-Dec): ").lower()
    sales = float(input("Enter sales amount: "))
    
    # Calling the function
    next_sales = comp_forecast(month, sales)
    
    # Results
    print("Last Name:", last_name)
    print("Next Months Forecast: $", format(next_sales, ".2f"))
    print()
    
    count += 1
    
    # Repeat ask
    response = input("Would you like to enter another? (Y/N): ").lower()
    
# Final output
print("Number of entries:", count)
    