#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    arr = [0] * (n+2)
    for i,b,k in queries:
        arr[i]+=k
        arr[b+1]-=k
        
    maximum = temp = 0
    for val in arr:
        temp+=val
        maximum = max(maximum,temp)
        
    return maximum

print(arrayManipulation(10,[[1,5,3],[4,8,7],[6,9,1]]))
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     queries = []

#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = arrayManipulation(n, queries)

#     fptr.write(str(result) + '\n')

#     fptr.close()
