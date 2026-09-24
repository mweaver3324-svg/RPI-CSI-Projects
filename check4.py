# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:06:28 2026

@author: Michael
"""
#Creates adjusting asterisk border
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
max_length = max(len('Hello,'), len(first_name),len(last_name) + 6)
stars = '*' * max_length
print(stars)
print('*' * 2, "Hello,", '*' * 2)
print('*' * 2, first_name, '  **')
print('*' * 2, last_name, '**')
print(stars)


