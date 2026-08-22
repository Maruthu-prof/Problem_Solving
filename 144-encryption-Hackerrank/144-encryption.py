#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Remove any existing spaces from the text
    s = s.replace(" ", "")
    L = len(s)
    
    # Calculate the number of columns using the ceiling of the square root
    columns = math.ceil(math.sqrt(L))
    
    output = []
    # Iterate through each column index
    for i in range(columns):
        # Collect characters at intervals of 'columns' size
        column_chars = [s[j] for j in range(i, L, columns)]
        output.append("".join(column_chars))
        
    # Join the columns with a single space separator
    return " ".join(output)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna