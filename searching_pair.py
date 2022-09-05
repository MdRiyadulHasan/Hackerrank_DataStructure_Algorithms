from collections import Counter
def pairs(k, arr):
    d=Counter(arr)
    print(d)
    c=0
    for i in arr:
        if i+k in d:
            c=c+1
        if i-k in d:
            c=c+1
        del d[i]
    
    return c

if __name__ == "__main__":
    n,k=list(map(int,input().strip().split()))
    arr=list(map(int,input().strip().split()))
    result = pairs(k,arr)
    print(result)