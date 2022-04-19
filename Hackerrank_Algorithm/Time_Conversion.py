#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    hour = s[0:2]
    rest = s[2:8]

    #AM
    if (s[8:] =="AM"):
        if (hour == "12"):
            hour = "00"

    #PM
    else:
        if (hour != "12"):
            hour = str(int(hour)+12)

    
    return hour+rest        

s = "06:40:03AM"
print(timeConversion(s))
