
import math
import os
import random
import re
import sys

# s,t : location of house
# a,b : location of apple tree and orange tree, repectively
# apples: integer array, distance where fallen
# oranges: integer array, distance where fallen


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple = 0
    orange = 0

    # apples_fallen = apples + a
    # oranges_fallen = oranges + b

    for i in apples:
        i = i+a
        if (i>= s and i<=t):
            apple = apple + 1
        else:
            continue

    for j in oranges:
        j = j+b
        if (j>= s and j<=t):
            orange = orange + 1
        else:
            continue

    print(apple)
    print(orange)

countApplesAndOranges(7,13,5,15,[-2,2,1],[5,-6])