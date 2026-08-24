#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Create a frequency map of all numbers in the array
    counts = Counter(arr)
    total_triplets = 0
    
    # Iterate through unique numbers to find valid sequences
    for val in counts:
        if (val + d) in counts and (val + 2 * d) in counts:
            # Multiply frequencies to get all possible index combinations
            total_triplets += counts[val] * counts[val + d] * counts[val + 2 * d]
            
    return total_triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna