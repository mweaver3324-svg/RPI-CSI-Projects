# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:59:33 2026

@author: Michael
"""
#Madlibs game
name = input("Enter your name:")
adjective1 = input("Enter an adjective:")
adjective2 = input("Enter another adjective:")
adjective3 = input("Enter a final adjective:")
noun1 = input("Enter a noun:")
noun2 = input("Enter another noun:")
noun3 = input("Enter a third noun:")
noun4 = input("Enter a final noun:")
verb1 = input("Enter a verb:")
verb2 = input("Enter another verb:")
verb3 = input("Enter a final verb:")
emotion1 = input("Enter an emotion:")
emotion2 = input("Enter another emotion:")
season = input("Enter a season:")
teamname = input("Enter a team name:")
# + concatenation resolves improper spacing
print("\n\nGood morning",name+"!" " This will be a/an", adjective1, noun1+'.' " Are you", verb1, "forward to it?") 
print("You will", verb2, "a lot of", noun2, "and feel "+emotion1, "when you do.")
print("If you do not, you will", verb3, "this", noun3)
print("This", season, "was",adjective2+'.' ' Were you '+emotion2, "when",teamname, "won\n""the",noun4+"?")
print("\n Have a/an",adjective3,"day!")

