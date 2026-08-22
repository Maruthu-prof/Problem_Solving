#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Convert string to list for mutability
    arr = list(w)
    n = len(arr)
    
    # Step 1: Find the largest index i such that arr[i] < arr[i + 1]
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
        
    # If no such index exists, the string is in descending order (highest possible permutation)
    if i < 0:
        return "no answer"
        
    # Step 2: Find the largest index j greater than i such that arr[i] < arr[j]
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1
        
    # Step 3: Swap the characters at index i and j
    arr[i], arr[j] = arr[j], arr[i]
    
    # Step 4: Reverse the suffix starting right after index i
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return "".join(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna