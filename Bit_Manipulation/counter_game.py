import math
import os
import random
import re
import sys
def counterGame(n):
    setbits=bin(n-1).count('1')
    if(setbits&1):
        return 'Louise'
    else:
        return 'Richard'
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = counterGame(n)
        print(result)
