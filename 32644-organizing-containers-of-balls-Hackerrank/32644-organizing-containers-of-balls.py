#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Calculate the total capacity of each container (sum of each row)
    container_capacities = [sum(row) for row in container]
    
    # Calculate the total quantity of each ball type (sum of each column)
    n = len(container)
    ball_type_totals = [sum(container[row][col] for row in range(n)) for col in range(n)]
    
    # Sort both distributions to compare them directly
    container_capacities.sort()
    ball_type_totals.sort()
    
    # If the multisets match, a successful organization is possible
    if container_capacities == ball_type_totals:
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna