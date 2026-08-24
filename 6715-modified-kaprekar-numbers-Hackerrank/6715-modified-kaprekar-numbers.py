#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    results = []
    for i in range(p, q + 1):
        d = len(str(i))
        sq_str = str(i * i)

        # Split into right part of length d and left part containing the remaining digits
        right = sq_str[-d:]
        left = sq_str[:-d] if sq_str[:-d] else "0"

        # Check if the sum of both parts equals the original number
        if int(left) + int(right) == i:
            results.append(i)

    # Print space-separated numbers or INVALID RANGE if none exist
    if results:
        print(*results)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna