#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:06:38 2026

@author: abealansari
"""

# Global list to store dogs
dogs = []

# function to add dog
def addDog():
    print("\n--- Add a Dog ---")
    
    name = input("Enter Dogs Name: ")
    breed = input("Enter Dogs Breed: ")
    age = input("Enter Dogs Age: ")
    weight = input("Enter Dogs Weight: ")
    
    # Store info in a list
    dog = [name, breed, age, weight]
    
    # Add dog to main dogs list
    dogs.append(dog)

    print("Dog added successfully!\n")

# function to view dogs
def viewDogs():
    print("\n--- View Dogs ---")

    # Check if list is empty
    if len(dogs) == 0:
        print("No dogs found.\n")
        return

    # Print headers
    print(f"{'Name':<15}{'Breed':<20}{'Age':<10}{'Weight':<10}")
    print("-" * 55)

    # Loop through dogs list
    for dog in dogs:
        print(f"{dog[0]:<15}{dog[1]:<20}{dog[2]:<10}{dog[3]:<10}")

    print()

# Function: Find Dog
def findDog():
    print("\n--- Find Dog ---")

    search_name = input("Enter dog name to search: ")

    found = False

    # Search through dogs list
    for dog in dogs:
        if dog[0].lower() == search_name.lower():

            print("\nDog Found!")
            print(f"Name: {dog[0]}")
            print(f"Breed: {dog[1]}")
            print(f"Age: {dog[2]}")
            print(f"Weight: {dog[3]}\n")

            found = True

    # If dog not found
    if found == False:
        print("Dog not found.\n")

# menu function
def menu():

    while True:

        print("===== Dog Rescue Menu =====")
        print("1. Add a Dog")
        print("2. View Dogs")
        print("3. Find Dog")
        print("4. Quit")

        choice = input("Enter your choice (1,2,3,4): ")

        # Menu options
        if choice == "1":
            addDog()

        elif choice == "2":
            viewDogs()

        elif choice == "3":
            findDog()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")

# main function
def main():
    
    print()
    print("Welcome to the Dog Rescue Application!\n")

    # Call menu
    menu()

# Start program
main()