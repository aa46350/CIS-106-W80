#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:03:31 2026

@author: abealansari
"""

# Function for loading file to dictionary
def load_players(filename):
    players = {}
    
    file = open(filename, "r")
    
    for line in file:
        line = line.strip()
        
        parts = line.split()
        
        name = parts[0]
        avg = float(parts[1])
        
        players[name] = avg
        
    file.close()
    return players

# Function to print dictionary
def print_players(player_dict):
    print(f"{'Player Name':<15} {'Batting Avg':<12}")
    print("-" * 27)
    
    for name in player_dict:
        print(f"{name:<15} {player_dict[name]:<12.3f}")

# Main code
players_dict = load_players("playersavgs.txt")
print_players(players_dict)
