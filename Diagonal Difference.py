# Name = Vipan Kumar
# user name = @VipanKumar01

import math
import os
import random
import re
import sys

# 1st Time complexity is : O(n)

def diagonalDifference(arr):
    temp1 = 0
    temp2 = 0
    for i in range(len(arr)):
        temp1 += arr[i][i]
    
    for i in range(len(arr)):
        temp2 += arr[i][n-i-1]
        
    difference = temp1 - temp2
    difference = abs(difference)
    return difference
  
# Name = Vipan Kumar
# user name = @VipanKumar01
#####################################
#------------------------------------

# You can use this method
# 2nd gives you Time Compexity : O(n^2)

  
'''
# 2nd
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                temp += arr[i][j]
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

    
    # --Happy Code--
