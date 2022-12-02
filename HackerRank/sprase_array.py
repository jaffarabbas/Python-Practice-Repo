#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY stringList
#  2. STRING_ARRAY queries
#
l1=["aba","baba","aba","xzxb"]
q1=["aba","xzxb","ab"]
def matchingStrings(stringList, queries):
    # Write your code here
    lst= []
    for j in queries:
        count = 0
        for i in stringList:
            if j == i:
                count+=1
        lst.append(count)
    return lst

print(matchingStrings(l1,q1))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     stringList_count = int(input().strip())

#     stringList = []

#     for _ in range(stringList_count):
#         stringList_item = input()
#         stringList.append(stringList_item)

#     queries_count = int(input().strip())

#     queries = []

#     for _ in range(queries_count):
#         queries_item = input()
#         queries.append(queries_item)

#     res = matchingStrings(stringList, queries)

#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')

#     fptr.close()
