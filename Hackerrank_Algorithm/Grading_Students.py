import math
import os
import random
import re
import sys



def gradingStudents(grades):

    new_grade = []

    for i in grades:
        round = ((i // 5)+1)*5
        difference = round - i

        if (i < 35 or difference >= 3 ):
            new_grade.append(i)
        elif (difference < 3):
            new_grade.append(round)
   
    return new_grade



s = [73,67,38,33]
print(gradingStudents(s))

