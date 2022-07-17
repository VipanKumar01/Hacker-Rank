# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    firstSum,secondSum = 0,0
    lengthArr = len(arr)
    
    arr = sorted(arr)
    
    for i in range(0,4):
        firstSum += arr[i]
    
    for i in range(lengthArr-4,len(arr)):
        secondSum += arr[i]
        
    print(firstSum,secondSum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

    
    
    # --HappyCode--
