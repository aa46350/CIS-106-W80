#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:14:00 2026

@author: abealansari
"""

total_extended = 0
count = 0

with open("/Users/abealansari/Documents/items.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip() != ""]

for i in range(0, len(lines), 3):
    try:
        item = lines[i]
        quantity = int(lines[i+1])
        price = float(lines[i+2])
    except (IndexError, ValueError):
        print("Skipping bad data near:", lines[i:i+3])
        continue

    extended = quantity * price

    total_extended += extended
    count += 1

    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Extended Price: ${extended:.2f}\n")

average = total_extended / count if count > 0 else 0

print(f"Total of Extended Prices: ${total_extended:.2f}")
print(f"Number of Orders: {count}")
print(f"Average Order: ${average:.2f}")