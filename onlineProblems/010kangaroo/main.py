# https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=false

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def checkJump(kOne, kTwo, jumpOne, jumpTwo):
    while kOne <= kTwo:
        kOne += jumpOne
        kTwo += jumpTwo
        if kOne == kTwo:
            return "YES"
    return "NO"

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    kOne = x1
    kTwo = x2
    jumpOne = v1
    jumpTwo = v2

    if jumpOne > jumpTwo:
        return checkJump(kOne, kTwo, jumpOne, jumpTwo)

    elif jumpOne < jumpTwo and kOne > kTwo:
        return checkJump(kOne, kTwo, jumpOne, jumpTwo)
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
