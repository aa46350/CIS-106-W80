#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:58:45 2026

@author: abealansari
"""

def comp_price(msrp, make, model, ev_code):
    
    make = make.lower()
    model = model.lower()
    ev_code = ev_code.lower()
    
    if ev_code in ("y", "yes"):
        percent = 0.30
    elif make == "honda" and model == "accord":
        percent = 0.10
    elif make == "toyota" and model == "rav4":
        percent = 0.15
    else:
        percent = 0.05
    
    discount = msrp * percent
    new_price = msrp - discount
    
    tax = new_price * 0.07
    total = new_price + tax
    
    return total

total_msrp = 0
total_sales = 0
count= 0

response = input("Do you want to enter car information? (Y/N): ").lower()

while response in ("y", "yes"):
    
    make = input("Enter the make of the car: ")
    model = input("Enter the model: ")
    ev_code = input("Is it an electric vehicle? (Y/N): ")
    msrp = float(input("Enter the MSRP: "))
    
    final_price = comp_price(msrp, make, model, ev_code)
    
    print("Make:", make)
    print("Model:", model)
    print("Price out-the-door: $", format(final_price, ".2f"))
    print()
    
    total_msrp += msrp
    total_sales += final_price
    count += 1
    
    response = input("Would you like to enter another car? (Y/N): ").lower()
    
print("Total MSRP: $", format(total_msrp, ".2f"))
print("Total Sales:  $", format(total_sales, ".2f"))
print("Number of cars entered:", count)
