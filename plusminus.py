#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n=len(arr)
    p=0
    m=0
    z=0
    for i in range(0,n):
        if (arr[i]>0):
            p=p+1
        elif (arr[i]<0):
            m=m+1
        else:
            z=z+1
    p= float(p)/float(n)
    m= float(m)/float(n)
    z= float(z)/float(n)
    print ("%.6f\n%.6f\n%.6f" %(p,m,z))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
