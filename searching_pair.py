def pairs(k, arr):
    arr.sort()
    c=0
    for i in range(n-1):
        for j in range (i+1,n):
            if abs(arr[i]-arr[j])==k:
                c=c+1
    return c

if __name__ == "__main__":
    n,k=list(map(int,input().strip().split()))
    arr=list(map(int,input().strip().split()))
    result = pairs(k,arr)
    print(result)