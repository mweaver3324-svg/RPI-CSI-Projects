# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:44:09 2026

@author: Michael
"""
frame = input("Frame character => ")
print(frame)
height = int(input("Height => "))
print(height)
width = int(input("Width => "))
print(width)
dimensions = str(width) + "x" + str(height)
top_bottom = frame * width
middle_row = (height - 2) // 2
above = middle_row - 1
below = height - 2 - above - 1
left_spaces = (width - 2 - len(dimensions)) // 2
right_spaces = width - 2 - len(dimensions) - left_spaces
blank_row = frame + " " * (width - 2) + frame
text_row = frame + " " * left_spaces + dimensions + " " * right_spaces + frame

box = (
top_bottom + "\n" +
(blank_row + "\n") * above +
text_row + "\n" +
(blank_row + "\n") * below +
top_bottom
)
print(box)