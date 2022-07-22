# Task
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# region  
# Input Format
# A single line containing a positive integer, n.

# Constraints
# 1 <= n <= 100

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input
# 3

# Sample output
# Weird

# Explanation
# n == 3
# n is odd and odd numbers are weird, so print Weird.

# endregion 
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter Number:").strip())
    #Assume n is 3 
    # Remainder = 4 % 2
    Remainder = n % 2
    if Remainder == 0:
        if (n >= 2 and n <= 5) or n > 20: 
            print("Not Weird")
       
        if n >= 6 and n <= 20:
            print("Weird") 
    else:
        print("Weird")
    print("Exiting Program")
    
