"""
A disorganized handyman has mixed up his nuts and bolts in a bag and your task is to match them as 
quickly as possible. 
"""
import random

n = int(input("Number of nut and bolts in total"))
nuts = [0]*n
bolts = [0]*n
types = int(input("The different categories of nuts and bolts available:"))
for i in range (n):
    number_generated = random.randint(1, types)
    nuts[i] = bolts[i] = number_generated
random.shuffle(bolts)

