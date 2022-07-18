# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


import math
import os
import random
import re
import sys


def lonelyinteger(a):
    j = 0
    for i in a:
        j ^= i
    else:
        return j
      
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    # --Happy Code--
