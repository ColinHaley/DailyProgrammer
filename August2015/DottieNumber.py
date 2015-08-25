"""
Author: Colin Haley
Purpose: Practice python development by participating in the Daily Programmer challenges from Reddit
"""

import math


# Main Challenge

def dottieNumber(counter=0):
    # Not needed but give the option to start at a non-zero number.
    # I'm going to detect when to stop based on the difference between the two numbers being < .0001
    # can use math.fabs() to detect this I think.
    now = counter
    next = counter + 1
    
    while abs(now - next) > 0.0001:
        now = next
        next = math.cos(next)

    # After the diff is hit, return the "next" value
    return next


print(dottieNumber())
