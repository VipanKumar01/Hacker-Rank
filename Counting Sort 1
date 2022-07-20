# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

import math
import os
import random
import re
import sys



def countingSort(arr):
    count = [0] *100
    for i in arr:
        count[i] += 1
    return count
    
    
# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
    
    # -- Happy Code --
