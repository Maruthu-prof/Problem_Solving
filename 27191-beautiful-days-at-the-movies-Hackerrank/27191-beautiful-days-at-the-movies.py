#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    beautiful_days_count = 0
    
    # Loop through each day in the inclusive range [i...j]
    for day in range(i, j + 1):
        # Reverse the day by converting it to a string, slicing, and turning it back to int
        reversed_day = int(str(day)[::-1])
        
        # Check if the absolute difference is evenly divisible by k
        if abs(day - reversed_day) % k == 0:
            beautiful_days_count += 1
            
    return beautiful_days_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna