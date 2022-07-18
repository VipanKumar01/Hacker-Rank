# Name = Vipan Kumar
# GitHub user name = @VipanKumar01

""" Please Help for improve that :- I Don't Know Where is Error is Occurs 
So Help me to Improve that 
The Error is Occurs in test cases :- 2nd, 4th, 6th test cases Only"""

import math
import os
import random
import re
import sys



def timeConversion(s):
    if "AM" in s:
        if "12" in s[0:2]:
            return "00" + s[2:-2]

    elif "PM" in s:
        if "01" in s[0:2]:
            return "13" + s[2:-2]
        
        elif "02" in s[0:2]:
            return "14" + s[2:-2]
        
    
        elif "03" in s[0:2]:
            return "15" + s[2:-2]
    
        elif "04" in s[0:2]:
            return "16" + s[2:-2]
    
        elif "05" in s[0:2]:
            return "17" + s[2:-2]
     
        elif "06" in s[0:2]:
            return "18" + s[2:-2]
     
        elif "07" in s[0:2]:
            return "19" + s[2:-2]
     
        elif "08" in s[0:2]:
            return "20" + s[2:-2]
     
        elif "09" in s[0:2]:
            return "21" + s[2:-2]
    
        elif "10" in s[0:2]:
            return "22" + s[2:-2]
    
        elif "11" in s[0:2]:
            return "23" + s[2:-2]
        else:
            return s
    else:
          return s  

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

# --Happy Code--
