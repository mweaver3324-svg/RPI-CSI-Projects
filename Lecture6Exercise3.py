# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:37:25 2026

@author: Michael
"""

first_number = float(input("Enter the first number: "))
print(first_number)
second_number = float(input("Enter the second number: "))
print(second_number)
if first_number and second_number > 10:
    print("Both are greater than 10.")
elif first_number and second_number < 10:
    print("Both are below 10.")
average_addition = first_number + second_number
average_division = average_addition/2
print("Average is",round(average_division, 2)) #Rounds to two decimal places if they exist
