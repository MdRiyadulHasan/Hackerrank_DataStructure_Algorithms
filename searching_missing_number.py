from collections import Counter
import numpy as np
def missingNumbers(arr,brr):
    a=Counter(arr)
    print(a)
    b=Counter(brr)
    print(b)
    c=b-a
    return sorted(c.keys())

if __name__ =='__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    result=np.asarray(result)
    print(result)