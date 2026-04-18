#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:01:52 2026

@author: abealansari
"""

def comp_discount(qty, amount, price):
    total = qty * price
    disc_amount = total * amount
    disc_price = total - disc_amount 
    
    return disc_price, disc_amount

qty = int(input("Enter the quantity: "))
amount = float(input("Enter the discount rate (as a decimal): "))
price = float(input("Enter the price of the item: "))

final_price, discount = comp_discount(qty, amount, price)

print("Quantity:", qty)
print("Price: $", format(price, ".2f"))
print("Discount amount: $", format(discount, ".2f"))
print("Discounted price: $", format(final_price, ".2f"))

