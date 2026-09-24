# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:02:48 2026

@author: Michael
"""

#Calculates pace and speed of a runner based on values given by the user
minutes = int(input("Minutes ==> "))
seconds = int(input("Seconds ==> "))
miles = float(input("Miles ==> "))
target_miles = float(input("Miles to target ==> "))
total_seconds = minutes * 60 + seconds

pace_seconds = total_seconds / miles
pace_minutes = int(pace_seconds // 60)
pace_remaining_seconds = int(pace_seconds % 60)

speed = miles / (total_seconds / 3600)

target_seconds = pace_seconds * target_miles
target_minutes = int(target_seconds // 60)
target_remaining_seconds = int(target_seconds % 60)
print()
print("Pace is {} minutes and {} seconds per mile.".format(
pace_minutes, pace_remaining_seconds))
print("Speed is {:.2f} miles per hour.".format(speed))

print("Time to run the target distance of {} miles is {} minutes and {} seconds.".format(
target_miles, target_minutes, target_remaining_seconds))

