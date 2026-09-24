# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:58:25 2026

@author: Michael
"""
#Creates asterisk border around the statement. Border size does not adjust to argument 'statement' length.
def frame_string(statement):
    
    border = '*' * 25
    print(border,'\n'"**", statement,"**")
    print(border,"\n")

frame_string("Spanish Inquisition")

def frame_string(statement):
    border = '*' * 8
    print(border)
    print("**", statement,"**")
    print(border)
    
frame_string("Ni")
    
